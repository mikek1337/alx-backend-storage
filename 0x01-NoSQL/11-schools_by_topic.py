#!/usr/bin/env python3
"""retrieve school by topic"""


def schools_by_topic(mongo_collection, topic):
    """retrieve school by topic"""
    return mongo_collection.find({"topics": topic})
