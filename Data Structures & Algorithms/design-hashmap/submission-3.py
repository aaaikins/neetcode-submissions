class MyHashMap:

    def __init__(self):
        self.capacity = 100000
        self.buckets = [[] for _ in range(self.capacity)]
        

    def put(self, key: int, value: int) -> None:
        key = key % self.capacity
        self.buckets[key] = value

    def get(self, key: int) -> int:
        key = key % self.capacity
        if self.buckets[key] == []:
            return -1 
        else:
            return self.buckets[key]
        

    def remove(self, key: int) -> None:
        key = key % self.capacity
        if self.buckets[key]:
            self.buckets[key] = []


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
        
        