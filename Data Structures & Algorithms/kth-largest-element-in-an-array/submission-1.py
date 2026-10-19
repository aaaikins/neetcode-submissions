import random

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        k = len(nums) - k

        def quickselect(l, r):
            # Randomize pivot
            rand_idx = random.randint(l, r)
            nums[rand_idx], nums[r] = nums[r], nums[rand_idx]

            pivot = nums[r]
            p = l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1

            nums[p], nums[r] = nums[r], nums[p]

            if k < p:
                return quickselect(l, p - 1)
            elif k > p:
                return quickselect(p + 1, r)
            else:
                return nums[p]

        return quickselect(0, len(nums) - 1)