#!/usr/bin/env python3
"""Redis caching module"""
import redis
from typing import Union, Callable
import uuid


def count_calls(method: Callable) -> Callable:
    """count how many times methods of the Cache class are called"""
    key = method.__qualname__

    def wrapper(self, *args, **kwargs):
        """wrapper function"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """class to handle caching by redis"""

    def __init__(self) -> None:
        """constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    @count_calls
    def store(self, data: Union[str, int, float, bytes]) -> str:
        """store data in redis"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable) -> Union[str, int, float, bytes]:
        """get data from redis"""
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> str:
        """get data from redis"""
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """get data from redis"""
       return self.get(key, lambda d: int(d))

