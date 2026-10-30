class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_map = {}

    def get(self, key: int) -> int:
        if key not in self.cache_map:
            return -1
        value = self.cache_map.pop(key)
        self.cache_map[key] = value
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.cache_map:
            self.cache_map.pop(key)
        elif len(self.cache_map) >= self.capacity:
            oldest_key = next(iter(self.cache_map))
            self.cache_map.pop(oldest_key)
        self.cache_map[key] = value        



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)