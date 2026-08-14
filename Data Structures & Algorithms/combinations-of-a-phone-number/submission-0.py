class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []

        result = []
        combination = []

        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }


        def backtrack(index):
            if index == len(digits):
                result.append("".join(combination))
                return 
            
            for char in mapping[digits[index]]:
                combination.append(char)

                backtrack(index + 1)

                combination.pop()

        backtrack(0)
        return result


            
