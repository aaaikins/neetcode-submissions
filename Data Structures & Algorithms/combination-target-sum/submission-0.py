class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(idx, total, comb):

            if total == target:
                result.append(comb[:])
                return
            
            for i in range(idx, len(nums)):
                # total += num
                if total > target:
                    continue
                comb.append(nums[i])
                backtrack(i, total + nums[i], comb)
                comb.pop()
        
        backtrack(0, 0, [])

        return result