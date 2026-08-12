class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        perms = []
        result = []
        
        def backtrack():

            if len(perms) == len(nums):
                result.append(perms.copy())
                return
            
            for num in nums:
                if num not in perms:
                    perms.append(num)
                    backtrack()
                    perms.pop()
            
        backtrack()
        return result

            