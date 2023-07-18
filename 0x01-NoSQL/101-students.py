#!/usr/bin/env python3
"""select top student"""


def top_students(mongo_collection):
    """select top student"""
    return mongo_collection.aggregate([
        {"$project": {"name": "$name", "averageScore": {"$avg": "$topics.score"}}},
        {"$sort": {"averageScore": -1}}
    ])
