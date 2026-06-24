class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest_streak = 0
        print(hashset)

        for num in nums:
            if (num - 1) not in hashset:
                current_streak = 0
                while num + current_streak in hashset:
                    current_streak += 1
                longest_streak = max(current_streak, longest_streak)
        return longest_streak