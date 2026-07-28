class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        for c in s:
            if c in closeToOpen:
                if len(stack) == 0 or stack[-1] != closeToOpen[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        
        return len(stack) == 0

        

