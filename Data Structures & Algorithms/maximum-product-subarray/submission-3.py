class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        result  = nums[0]
        curMax = nums[0]
        curMin = nums[0]
        
        for i in range(1, n):
            oldMax = curMax
            oldMin = curMin

            curMax = max(nums[i], nums[i] * oldMax, nums[i] * oldMin)
            curMin = min(nums[i], nums[i] * oldMax, nums[i] * oldMin)

            result = max(result, curMax)

        return result