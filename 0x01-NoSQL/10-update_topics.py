#!/usr/bin/env python3
"""updates a document in a collection based on its name"""


def update_topics(mongo_collection, name, topics):
    """updates a document in a collection based on its name"""
    return mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
