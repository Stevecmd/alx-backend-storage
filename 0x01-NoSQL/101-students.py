#!/usr/bin/env python3
""" 101-students.py """


def top_students(mongo_collection):
    """
    Returns all students sorted by average score
    :param mongo_collection: pymongo collection object
    :return: list of students sorted by average score
    """
    pipeline = [
        {
            "$project": {
                "name": 1,
                "topics": 1,
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ]
    return list(mongo_collection.aggregate(pipeline))
