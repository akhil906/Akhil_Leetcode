class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [amount+1] * (amount+1)
        dp[0] = 0
        print(len(dp))

        
        for a in range(1,len(dp)):
            for c in coins:
                if a-c >= 0:
                    dp[a] = min(dp[a],1+dp[a-c])

                   
        if dp[amount] !=  amount+1:
            return dp[amount]
        else:
            return -1
                



        