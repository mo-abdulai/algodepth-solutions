class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = defaultdict(list)

        for str in strs:
            counts = [0] * 26
            for ch in str:
                counts[ord(ch) - ord('a')] += 1
            
            key = tuple(counts)
            groups[key].append(str)
        
        return list(groups.values())