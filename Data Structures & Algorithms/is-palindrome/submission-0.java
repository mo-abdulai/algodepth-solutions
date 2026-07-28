class Solution {
    public boolean isPalindrome(String s) {

        if(s.length() == 0) return true;

        s = s.toLowerCase().replaceAll("[^A-Za-z0-9]", "");

        int r = 0;
        int l = s.length() - 1;

        while(r < l){
            if (s.charAt(r) != s.charAt(l)){
                return false;
            }
            else{
                r++;
                l--;
            }


        }
        return true;   
    }
}
