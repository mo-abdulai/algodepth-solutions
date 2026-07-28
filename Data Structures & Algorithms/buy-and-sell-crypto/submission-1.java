class Solution {
    public int maxProfit(int[] prices) {

        int buyPrice = prices[0];
        int profit = 0;

        for(int i = 0; i < prices.length; i++){
            if(prices[i] < buyPrice){
                buyPrice  = prices[i];
            }

            else {
                int currentPrice = prices[i] - buyPrice;
                profit = Math.max(currentPrice, profit);
            }
        }

        return profit;
    }
}

// Time complexity: 0(n)
// Space Complexity: 0(1)