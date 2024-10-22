#!/usr/bin/env python3
""" schools by topic """


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic
    :param mongo_collection: pymongo collection object
    :param topic: topic searched
    :return: list of schools with the specific topic
    """
    return list(mongo_collection.find({"topics": topic}))
