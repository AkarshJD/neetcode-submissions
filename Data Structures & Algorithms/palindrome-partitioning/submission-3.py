class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        #index needed - and no variable passing needed
        def dfs(i):
            #base case
            if(i >= len(s)):
                #If we use different recursive calls, since we 
                # have only one partition we need copies
                res.append(part.copy())
            for j in range(i, len(s)):
                if self.isPali(s, i , j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()

        dfs(0)
        return res
    
    def isPali(self, s, l, r):
        while(l < r):
            if s[l] != s[r]:
                return False
            l, r = l+1, r-1
        return True