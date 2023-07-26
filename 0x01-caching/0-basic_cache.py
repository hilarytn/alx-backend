#!/usr/bin/python3
""" 0-basic_cache """
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ BaseCache defines the methods to
      -put and
      -get the cached key-value pairs
    """

    def put(self, key, item):
        """Add an item to the cache"""
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
