class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []

        def backtrack(idx, total, comb):

            if total == target:
                result.append(comb[:])
                return
            
            for i in range(idx, len(nums)):
                # total += num
                if i > idx and nums[i - 1] == nums[i]:
                    continue
    
                if total + nums[i] > target:
                    break

                comb.append(nums[i])
                backtrack(i + 1, total + nums[i], comb)
                comb.pop()
        
        backtrack(0, 0, [])

        return result