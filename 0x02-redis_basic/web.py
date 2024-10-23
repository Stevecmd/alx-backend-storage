#!/usr/bin/env python3
""" Module to get HTML content of a URL and cache it """
import requests
import redis
from typing import Callable
from functools import wraps

# Initialize Redis client
redis_client = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """Decorator to count the number of requests to a URL"""
    @wraps(method)
    def wrapper(url: str) -> str:
        """Wrapper function to count requests and cache the result"""
        redis_client.incr(f"count:{url}")
        cached_content = redis_client.get(url)
        if cached_content:
            return cached_content.decode("utf-8")
        result = method(url)
        redis_client.setex(url, 10, result)
        return result
    return wrapper


@count_requests
def get_page(url: str) -> str:
    """Get the HTML content of a URL and cache it"""
    response = requests.get(url)
    return response.text


# Example usage
if __name__ == "__main__":
    url = (
        "http://slowwly.robertomurray.co.uk/delay/5000/"
        "url/http://www.example.com"
    )
    print(get_page(url))
    print(redis_client.get(f"count:{url}"))
    print(get_page(url))
    print(redis_client.get(f"count:{url}"))
