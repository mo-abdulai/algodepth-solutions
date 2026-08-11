class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []

        candidates.sort()

        def backtrack(index, curr, total):
            if total == target:
                result.append(curr.copy())
                return
            
            if total > target or index == len(candidates):
                return
            
            curr.append(candidates[index])

            backtrack(index + 1, curr, total + candidates[index])

            curr.pop()

            while  index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1
            
            backtrack(index + 1, curr, total)

        backtrack(0, [], 0)
        return result