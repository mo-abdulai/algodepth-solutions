class Solution {
    public int lengthOfLongestSubstring(String s) {

        int r = 0, l = 0, max = 0;

        Set<Character> set = new HashSet<>();

        while(r < s.length()){
            if(!set.contains(s.charAt(r))){
                set.add(s.charAt(r));
                max = Math.max(max, set.size());
                r++;
            }
            else{
                set.remove(s.charAt(l));
                l++;
            }

        }
       return max;
        
    }
}
