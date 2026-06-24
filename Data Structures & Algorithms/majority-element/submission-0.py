class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        print(count)

        freq = [(val, num) for num, val in count.items()]

        cnt, num = max(freq, key = lambda x: x[0])

        print(num)

        return num
        