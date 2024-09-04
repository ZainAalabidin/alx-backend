#!/usr/bin/env python3
''' FIFO caching.
'''

from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    ''' inherits from BaseCaching and is a caching system.
    '''

    def __init__(self):
        '''initialize the FIFO cache'''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''assign to the dictionary self.cache_data the item value
        for the key key.  '''
        if key is not None and item is not None:
            if key in self.cache_data:
                del self.cache_data[key]

            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first_key, _ = self.cache_data.popitem()
                print(f"DISCARD: {first_key}")
            self.cache_data[key] = item

    def get(self, key):
        '''return the value in self.cache_data linked to key.'''
        return self.cache_data.get(key, None)
