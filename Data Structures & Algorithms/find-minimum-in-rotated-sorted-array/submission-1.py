class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        
        if len(nums) <= 1:
            return nums[0]

        while start <= end:
            mid = (start+end) // 2

            if nums[mid + 1] < nums[mid]:
                return nums[mid + 1]
            
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            
            if nums[end] > nums[mid]:
                end = mid - 1
            else: 
                start = mid + 1

                 

        