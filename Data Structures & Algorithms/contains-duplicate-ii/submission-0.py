class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        left = 0
        numset = set()

        for right in range(len(nums)):
            if right - left > k:
                numset.remove(nums[left])
                left += 1
            if nums[right] in numset:
                return True
            numset.add(nums[right])
        
        return False
        