class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        # dp = [0] * n
        # dp[0] = nums[0] # dp[i -2]
        a = nums[0]
        # dp[1] = max(nums[0], nums[1]) # dp[i - 1]
        b = max(nums[0], nums[1])

        for i in range(2, n):
            # dp[i] = max(dp[i-1], dp[i - 2] + nums[i])
            a, b = b, max(b, a + nums[i])

        return b