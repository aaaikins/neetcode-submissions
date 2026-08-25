from heapq import heapify, heappop

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for p in points:
            x, y = p
            dist = x**2 + y**2

            heap.append((dist, p))
        
        heapify(heap)

        res = []

        while len(res) < k:
            dist, p = heappop(heap)
            res.append(p)
        
        return res