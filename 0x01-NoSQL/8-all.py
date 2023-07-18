#!/usr/bin/env python3
"""list all data in the collection"""


def list_all(mongo_collection):
    """list all data in the collection"""
    return mongo_collection.find()
