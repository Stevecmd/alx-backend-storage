#!/usr/bin/env python3
"""Provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


def log_stats():
    """Provides some stats about Nginx logs stored in MongoDB"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    # Total number of logs
    print(f"{nginx_collection.count_documents({})} logs")

    # Methods stats
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"    method {method}: {count}")

    # Status check count (documents with method=GET and path=/status)
    status_checks = nginx_collection.count_documents({
        "method": "GET",
        "path": "/status"
    })
    print(f"{status_checks} status check")


if __name__ == "__main__":
    log_stats()
