#!/usr/bin/env python3
"""Redis caching module"""
import redis
from typing import Union, Callable
import uuid


class Cache:
    """class to handle caching by redis"""

    def __init__(self) -> None:
        """constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, int, float, bytes]) -> str:
        """store data in redis"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get_str(self, key: str) -> str:
        """get data from redis"""
        data = self._redis.get(key)
        if data is not None:
            return data.decode('utf-8')
        return ""

    def get_int(self, key: str) -> int:
        """get data from redis"""
        data = self._redis.get(key)
        if data is not None:
            return int(data.decode('utf-8'))
        return 0

    def get(self, key: str, fn: Callable) -> str:
        """get data from redis"""
        data = self._redis.get(key)
        if data is not None:
            return fn(data)
        return ""
