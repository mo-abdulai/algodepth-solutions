class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        maxlength = 0
        maxfreq = 0
        left = 0

        for right, c  in enumerate(s):
            freq[c] = freq.get(c, 0) + 1

            maxfreq = max(maxfreq, freq[c])

            while (right - left + 1) - maxfreq > k:
                freq[s[left]] -= 1
                left += 1
            
            maxlength = max(maxlength, right - left + 1)
            
        return maxlength


