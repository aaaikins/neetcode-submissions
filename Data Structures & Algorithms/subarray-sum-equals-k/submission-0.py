class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums) 
        running_sum = 0
        seen = {0:1}
        res = 0

        for i in range(n):
            running_sum += nums[i]

            if running_sum - k in seen:
                res += seen[running_sum - k]

            seen[running_sum] = seen.get(running_sum, 0) + 1
        
        return res


