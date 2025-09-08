class MyHashSet:
    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size
    def add(self, key):
        bucket_index = self._hash(key)
        if key not in self.buckets[bucket_index]:
            self.buckets[bucket_index].append(key)

    def contains(self, key):
        bucket_index = self._hash(key)
        return key in self.buckets[bucket_index]

    def remove(self, key):
        bucket_index = self._hash(key)
        if key in self.buckets[bucket_index]:
            self.buckets[bucket_index].remove(key) 
