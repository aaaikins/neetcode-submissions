from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))
        
        dist = {i: float('inf') for i in range(1, n + 1)}
        dist[k] = 0

        min_heap = [(0, k)]

        while min_heap:
            d, node = heappop(min_heap)

            if d > dist[node]:
                continue

            for nei, weight in graph[node]:
                new_dist = d + weight

                if new_dist < dist[nei]:
                    dist[nei] = new_dist

                    heappush(min_heap, (new_dist, nei))
        print(dist)
        res = max(dist.values())

        return res if res != float('inf') else -1


        