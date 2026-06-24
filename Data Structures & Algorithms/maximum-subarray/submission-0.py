class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        maxSum = -float('inf')

        for num in nums:
            total += num
            maxSum = max(total, maxSum)

            if total < 0:
                total = 0
        

        return maxSum