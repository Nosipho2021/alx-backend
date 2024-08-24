#!/usr/bin/env python3
"""First-In First-Out caching module.
"""
from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Represents a caching system with a FIFO (First-In First-Out)
    removal mechanism when the limit is reached.
    """

    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item in the cache.
        Removes the first item in the cache if the size exceeds the limit.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first_key, _ = self.cache_data.popitem(False)
                print("DISCARD:", first_key)
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item by key.
        Returns None if the key does not exist.
        """
        return self.cache_data.get(key)
