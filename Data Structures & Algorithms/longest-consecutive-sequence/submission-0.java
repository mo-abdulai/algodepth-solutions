class Solution {
    public int longestConsecutive(int[] nums) {
        int max = 0;
        Set<Integer> set = new HashSet<>();
        
        for(int num : nums){
            set.add(num);
        }


        for(int num : nums){
            if(!set.contains(num - 1)){
                int start = num;


                while(set.contains(start)){
                    start++;
                }
            
            max = Math.max(max, start - num);

            }
        }
        return max;
}
    }
    
