class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasSet = set()

        for num in nums:
            if num in hasSet:
                return True
            hasSet.add(num)
        
        return False
        