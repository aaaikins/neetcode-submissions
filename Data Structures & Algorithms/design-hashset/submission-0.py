class MyHashSet:
    def __init__(self):
        self.capacity = 1
        self.buckets = [[] for _ in range(self.capacity)]
        
    def add(self, key: int) -> None:
        if not self.contains(key):
            index = key % self.capacity
            self.buckets[index].append(key)
        
    def remove(self, key: int) -> None:
        if self.contains(key):
            index = key % self.capacity
            self.buckets[index].remove(key)

    def contains(self, key: int) -> bool:
        index = key % self.capacity
        return key in self.buckets[index]
        
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)