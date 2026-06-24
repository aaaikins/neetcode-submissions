import heapq as hq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        hq.heapify(nums)
        while len(nums) > k:
            hq.heappop(nums)
        self.nums = nums
        print(self.nums)

    def add(self, val: int) -> int:
        hq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            hq.heappop(self.nums)
        print(self.nums)
        return self.nums[0]

        
