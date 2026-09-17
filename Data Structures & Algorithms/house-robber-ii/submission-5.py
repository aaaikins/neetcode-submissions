class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 2:
            return nums[0]

        def helper(nums):
            n = len(nums)
            dp = [0]*(n + 1)

            dp[1] = nums[0]
            # dp[2] =z
            for i in range(2, n + 1):
                dp[i] = max(dp[i - 1], nums[i - 1] + dp[i - 2])
            
            # print(dp)
            
            return dp[n]
        
        return max(helper(nums[:n - 1]), helper(nums[1:]))