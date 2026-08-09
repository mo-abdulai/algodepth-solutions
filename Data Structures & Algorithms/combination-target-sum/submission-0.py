class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        combination = []
        result = []

        def backtrack(index: int, remaining: int) -> None:
            if remaining == 0:
                result.append(combination.copy())
                return 

            if remaining < 0 or index == len(nums):
                return
            
            combination.append(nums[index])

            backtrack(index, remaining - nums[index])

            combination.pop()

            backtrack(index + 1, remaining)

        backtrack(0, target)
        return result
        