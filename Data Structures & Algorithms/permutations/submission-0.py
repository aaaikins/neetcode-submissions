class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(idx, perm):
            if idx == len(nums):
                result.append(perm[:])
                return

            for i in range(idx, len(nums)):
                nums[idx], nums[i] = nums[i], nums[idx]
                backtrack(idx + 1, perm)
                nums[idx], nums[i] = nums[i], nums[idx]
        
        backtrack(0, nums)

        return result