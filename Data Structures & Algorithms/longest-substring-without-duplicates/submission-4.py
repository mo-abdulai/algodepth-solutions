class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        left = 0
        maxlength = 0

        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[left])
                left += 1
            charset.add(s[r])

            maxlength = max(maxlength, r - left + 1)
        
        return maxlength

        