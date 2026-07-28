class Solution {
    public int maxArea(int[] heights) {

      

        int left = 0;
        int right = heights.length - 1;
        int water = 0;


        while(left < right){

           int maxArea = Math.min(heights[left], heights[right]) * (right - left);

            water = Math.max(maxArea, water);

            if(heights[left] < heights[right]){
                left++;
            }
            else{
                right--;
            }

        }
        
        return water;
    }
}
