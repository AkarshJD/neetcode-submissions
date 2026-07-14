class Solution:
    def numDecodings(self, s: str) -> int:
        #dp solution
        dp = { len(s): 1 }

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
            
            if (i + 1 < len(s) and (s[i] == "1" or
                s[i] == "2" and s[i + 1] in "0123456")):
                dp[i] += dp[i + 2]

        return dp[0]



        # #Recursive cachine solution
        # #base case if len of string is empty
        # dp = { len(s) : 1 }

        # def dfs(i):
        #     #Good base case
        #     if i in dp:
        #         return dp[i]
        #     #bad base case
        #     if s[i] == "0":
        #         return 0 

        #     #between 1 to 9
        #     res = dfs(i + 1)
        #     #check drawing explanation 10-26
        #     if (i + 1 < len(s) and (s[i] =="1" or
        #         s[i] == "2" and s[i + 1] in "0123456")):
        #         res += dfs(i + 2)
        #     #cache
        #     dp[i] = res
        #     return res
        
        # return dfs(0)