import heapq as hq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        hq.heapify(heap)

        while len(heap) > 1:
            print(heap)
            x = hq.heappop(heap)
            y = hq.heappop(heap)
            if y > x:
                # y = y - x
                hq.heappush(heap, x-y)

        return -hq.heappop(heap) if heap else 0
        