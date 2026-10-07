class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1

        return max(counts, key=counts.get)
        

