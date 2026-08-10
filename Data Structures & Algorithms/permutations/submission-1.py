class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        perm = []
        used = set()
        
        def backtrack():
            if len(perm) == len(nums):
                result.append(perm.copy())
                return
            
            for num in nums:
                if num not in perm:
                    perm.append(num)
                    backtrack()
                    perm.pop()
        
        backtrack()
        return result