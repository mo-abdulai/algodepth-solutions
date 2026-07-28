class Solution {
    public int maxArea(int[] heights) {
        int water = 0;
        int left = 0; 
        int right = heights.length - 1;

        while(left < right){

            int maxArea = Math.min(heights[left], heights[right]) * (right - left);
            water = Math.max(water, maxArea);

            if(heights[left] < heights[right]){
                left++;
            }else
                right--;
        }

        return water;
        
    }
}
