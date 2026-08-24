class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        longest = 0
        left = 0

        maxfreq = 0

        freq = {}

        # freq = Counter(s)

        for right, c in enumerate(s):

            freq[c] = freq.get(c, 0) + 1
            
            maxfreq = max(maxfreq, freq[c])

            while (right - left + 1) - maxfreq > k:
                freq[s[left]] -= 1
                left += 1
            
            longest = max(longest, right - left + 1)
        
        return longest
            

