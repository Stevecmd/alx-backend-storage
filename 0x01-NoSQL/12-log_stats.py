#!/usr/bin/env python3
"""Provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


def log_stats():
    """Provides some stats about Nginx logs stored in MongoDB"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    # Total number of logs
    total_logs = collection.count_documents({})
    print("{} logs".format(total_logs))

    # Methods stats
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))

    # Number of documents with method=GET and path=/status
    status_check = collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print("{} status check".format(status_check))

    # Get top 10 IPs
    print("IPs:")
    pipeline = [
        {
            "$group": {
                "_id": "$ip",
                "totalRequests": {"$sum": 1}
            }
        },
        {
            "$sort": {"totalRequests": -1}
        },
        {
            "$limit": 10
        }
    ]

    top_ips = collection.aggregate(pipeline)

    for ip_info in top_ips:
        ip = ip_info['_id']
        count = ip_info['totalRequests']
        print("\t{}: {}".format(ip, count))


if __name__ == "__main__":
    log_stats()
