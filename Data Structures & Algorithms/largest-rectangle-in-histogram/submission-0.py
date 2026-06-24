class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                area = height * (i - idx)
                maxArea = max(area, maxArea)
                start = idx

            stack.append((start, h))
        
        for i, h in stack:
            area = h * (len(heights) - i)
            maxArea = max(maxArea, area)

        return maxArea