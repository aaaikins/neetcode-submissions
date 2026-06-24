from heapq import heapify, heappush, heappop

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = []
        for cnt, char in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
            if cnt != 0:
                maxHeap.append([cnt, char])
        heapify(maxHeap)

        res = ""

        while maxHeap:
            cnt1, char1 = heappop(maxHeap)

            if len(res) >= 2 and res[-1] == res[-2] == char1:
                if not maxHeap:
                    break
                cnt2, char2 = heappop(maxHeap)
                res += char2
                cnt2 += 1
                if cnt2 < 0:
                    heappush(maxHeap, [cnt2, char2])
                heappush(maxHeap, [cnt1, char1])
            else:
                res += char1
                cnt1 += 1
                if cnt1 < 0:
                    heappush(maxHeap, [cnt1, char1])

        return res