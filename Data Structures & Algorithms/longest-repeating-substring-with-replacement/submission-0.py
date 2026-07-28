class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequency = {}
        maxlength = 0
        maxfrequency = 0
        left = 0

        for right, c in enumerate(s):
            frequency[c] = frequency.get(c, 0) + 1

            maxfrequency = max(maxfrequency, frequency[c])

            while (right - left + 1) - maxfrequency > k: 
                frequency[s[left]] -= 1
                left += 1
            
            maxlength = max(maxlength, (right  - left + 1))
        
        return maxlength

