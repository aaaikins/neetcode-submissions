class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0

        for num in nums:
            if num - 1 not in nums:
                cur = 0
                while num + cur in nums:
                    cur += 1
                longest = max(cur, longest)

        return longest
        