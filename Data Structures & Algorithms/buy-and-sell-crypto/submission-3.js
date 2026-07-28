class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {

        let buyPrice = prices[0];
        let profit = 0;

        for(let i = 0; i < prices.length; i++){

            if(prices[i] < buyPrice){
                buyPrice = prices[i];
            }
            else{
                let currentPrice = prices[i] - buyPrice;
                profit = Math.max(profit, currentPrice);
            }
        }

        return profit

    }
}
