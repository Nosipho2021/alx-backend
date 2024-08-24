#!/usr/bin/env python3
"""Basic caching module.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Represents a basic caching system that allows
    """

    def put(self, key: str, item: any) -> None:
        """Adds an item in the cache.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key: str) -> any:
        """Retrieves an item by key.
        """
        return self.cache_data.get(key, None)

