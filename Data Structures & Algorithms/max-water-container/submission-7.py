class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left  = 0
        right = len(heights) - 1

        water = 0

        while left < right:
            maxarea = min(heights[left], heights[right]) * (right - left)

            water = max(maxarea, water)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        

        return water