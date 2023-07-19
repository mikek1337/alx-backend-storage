#!/usr/bin/env python3
"""Redis caching module"""
import redis
from typing import Union
import uuid
class Cache:
    """class to handle caching by redis"""
    def __init__(self) -> None:
        """initialize redis client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self,data: Union[str, int, float, bytes])->str:
        """store data in redis"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
        