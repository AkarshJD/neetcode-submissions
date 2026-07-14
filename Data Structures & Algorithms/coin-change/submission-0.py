class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1) #Any max value
        dp[0] = 0
        #bottom up
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
                    # coin = 4
                    # a = 7
                    # dp[7] = 1 + dp[3]
        #only return if the value stored is not the default value
        return dp[amount] if dp[amount] != amount + 1 else -1