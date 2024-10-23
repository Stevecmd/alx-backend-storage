#!/usr/bin/env python3
""" Writing strings to Redis """
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Decorator that counts the number of calls to a method"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function that increments the call count"""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator that stores the history of
        inputs and outputs for a function"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function that stores inputs and outputs"""
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(output))
        return output
    return wrapper


def replay(method: Callable):
    """Display the history of calls of a particular function"""
    redis_client = method.__self__._redis
    method_name = method.__qualname__
    input_key = f"{method_name}:inputs"
    output_key = f"{method_name}:outputs"

    inputs = redis_client.lrange(input_key, 0, -1)
    outputs = redis_client.lrange(output_key, 0, -1)

    print(f"{method_name} was called {len(inputs)} times:")
    for input_data, output_data in zip(inputs, outputs):
        input_str = input_data.decode("utf-8")
        output_str = output_data.decode("utf-8")
        print(f"{method_name}(*{input_str}) -> {output_str}")


class Cache:
    """ Cache class """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store data in redis """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
        self, key: str, fn: Optional[Callable] = None
    ) -> Union[str, bytes, int, float, None]:
        """ Retrieve data from redis and optionally convert it """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """ Retrieve a string from redis """
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """ Retrieve an integer from redis """
        return self.get(key, int)


# Example usage
if __name__ == "__main__":
    cache = Cache()

    s1 = cache.store("foo")
    print(s1)
    s2 = cache.store("bar")
    print(s2)
    s3 = cache.store(42)
    print(s3)

    replay(cache.store)
