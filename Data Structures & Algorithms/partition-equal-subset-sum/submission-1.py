class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        dp =set()
        dp.add(0)

        target = sum(nums) // 2

        for _, num in enumerate(nums):
            nextdp = set()
            
            for t in dp:
                nextdp.add(t + num)
                nextdp.add(t)
            dp = nextdp

        return True if target in dp else False

            

        
       
        