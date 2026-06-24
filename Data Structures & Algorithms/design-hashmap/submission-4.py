class MyHashMap:

    def __init__(self):
        self.buckets = [[]] * 1000001

    def put(self, key: int, value: int) -> None:
        self.buckets[key] = value

    def get(self, key: int) -> int:
        if self.buckets[key] == []:
            return -1 
        else:
            return self.buckets[key]
        

    def remove(self, key: int) -> None:
        if self.buckets[key] != []:
            self.buckets[key] = []


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
        
        