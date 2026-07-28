class Solution {
    public int longestConsecutive(int[] nums) {

        Set<Integer> set = new HashSet<>();

        int max = 0;

        for( int num : nums){
            set.add(num);
        }


        for(int num : nums){

            if(!set.contains(num - 1)){
                int start = 0;
                while(set.contains(num + start)){
                    start++;
                }

                max = Math.max(max, start);
            }


        }
        

        return max;
    }
}
