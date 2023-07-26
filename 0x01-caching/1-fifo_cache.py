#!/usr/bin/python3
""" 1-fifo_cache """
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """First-In-First-Out Caching"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Add an item to the cache"""
        if key is None or item is None:
            pass
        elif len(self.cache_data) < BaseCaching.MAX_ITEMS:
            self.cache_data[key] = item
        elif key in self.cache_data:
                self.cache_data[key] = item
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            k = sorted(self.cache_data.keys())
            discard = self.cache_data.pop(k[0])
            print('Discard:', k[0])
            self.cache_data[key] = item   
        
    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]