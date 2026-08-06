class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        nums.sort()

        for i in range(len(nums)):
            return nums[i -k]


        


