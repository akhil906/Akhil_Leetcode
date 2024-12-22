class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = 0
        # stack = []
        # for i  in range(len(prices)):
        #     if not stack:
        #         stack.append(i)
            
        #     if stack[-1] > i:
        #         stack.pop(-1)
        #         stack.append(i)
        #     else:
        #         profit = max(profit,i-stack[-1])
        
        # return profit

        l , r = 0,1
        maxp = 0

        while r<len(prices):
            if prices[l]<prices[r]:
                profit = prices[r] - prices[l]
                maxp = max(maxp,profit)
            else:
                l = r
            r += 1
        
        return maxp
        




        