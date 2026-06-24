class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        leftHalf = nums[:mid]
        rightHalf = nums[mid:]

        sortedLeft = self.sortArray(leftHalf)
        sortedRight = self.sortArray(rightHalf)

        return self.merge(sortedLeft, sortedRight)

    def merge(self, left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result