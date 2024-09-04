#!/usr/bin/env python3
''' FIFO caching.
'''

from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    ''' inherits from BaseCaching and is a caching system.
    '''

    def __init__(self):
        '''initialize the FIFO cache'''
        super().__init__()
        self.cache_data = OrderedDict()
        self.usage_frequency = OrderedDict()

    def put(self, key, item):
        '''assign to the dictionary self.cache_data the item value
        for the key key.  '''
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.usage_frequency[key] += 1
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    min_freq = min(self.usage_frequency.values())
                    lfu_keys = [
                            k for k, v in self.usage_frequency.items()
                            if v == min_freq
                    ]

                    if len(lfu_keys) > 1:
                        lfu_key = next(
                            iter(k for k in self.cache_data if k in lfu_keys)
                        )
                    else:
                        lfu_key = lfu_keys[0]

                    del self.cache_data[lfu_key]
                    del self.usage_frequency[lfu_key]
                    print(f"DISCARD: {lfu_key}")

                self.cache_data[key] = item
                self.usage_frequency[key] = 1

    def get(self, key):
        '''return the value in self.cache_data linked to key.'''
        if key is None or key not in self.cache_data:
            return None

        self.usage_frequency[key] += 1
        return self.cache_data[key]
