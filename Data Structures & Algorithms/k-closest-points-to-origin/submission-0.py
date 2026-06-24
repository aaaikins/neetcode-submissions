import heapq as hq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            dist = (point[0])**2 + (point[1])**2
            heap.append((dist, point))
        
        hq.heapify(heap)
        # print(heap)

        res = []
        while k:
            dist, point = hq.heappop(heap)
            res.append(point)
            k -= 1
        return res


        