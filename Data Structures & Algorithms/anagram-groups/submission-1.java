class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        Map<String, List<String>> map = new HashMap<>();

        for (var str : strs){
            char [] ch = str.toCharArray();
            Arrays.sort(ch);
            String key = Arrays.toString(ch);

            map.putIfAbsent(key, new ArrayList<>());
            map.get(key).add(str);
        }

        return new ArrayList(map.values());
        
    }
}


// Time Complexity: 0(n k logk)
// Space Complexity: 0(n k) n is the number of string and k is the length of the string