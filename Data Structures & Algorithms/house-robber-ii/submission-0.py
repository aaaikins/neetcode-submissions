class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        def helper(arr):
            if len(arr) == 1:
                return arr[0]
            a, b = 0, 0
            for i in range(len(arr)):
                a, b = b, max(b, a + arr[i])
            
            return b

        c = helper(nums[:n - 1])
        d = helper(nums[1:])

        return max(c, d)