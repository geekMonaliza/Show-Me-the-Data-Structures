from collections import OrderedDict

class LRU_Cache(object):

    def __init__(self, capacity=5):
        # Initialize class variables
        self.capacity = capacity
        self.cache_dict = OrderedDict()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.cache_dict:
            self.cache_dict.move_to_end(key)
            return self.cache_dict[key]
        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        self.cache_dict[key] = value
        self.cache_dict.move_to_end(key)
        if len(self.cache_dict) > self.capacity:
            self.cache_dict.popitem(last=False)


# Testcase1
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


print(our_cache.get(1))      # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))     # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

# Testcase2
our_cache2 = LRU_Cache(3)
our_cache2.get(10)  # -1

# Testcase3
our_cache2 = LRU_Cache(0)
our_cache2.set(10, 10)
print(our_cache.get(10))  # -1
