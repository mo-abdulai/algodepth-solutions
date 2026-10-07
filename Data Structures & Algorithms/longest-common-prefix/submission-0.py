class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        first = strs[0]

        for i in range(len(first)):
            char = first[i]

            for word in strs[1:]:
                if i == len(word) or word[i] != char:
                    return first[:i]
        return first
        
