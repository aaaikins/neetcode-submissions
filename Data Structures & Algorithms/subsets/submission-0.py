class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(index, subset):
            # Base Case
            if index == len(nums):
                result.append(subset[:])
                return
            
            # adding int to subset
            subset.append(nums[index])
            backtrack(index + 1, subset)

            # Undo
            subset.pop()
            backtrack(index + 1, subset)

         
        backtrack(0, [])

        return result