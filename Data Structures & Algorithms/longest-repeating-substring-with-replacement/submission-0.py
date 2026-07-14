class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1+ count.get(s[r],0)
            maxf = max(maxf, count[s[r]])
            #Check if current window is valid
            # WindowSize - numberWithMaxCount
            while(r - l + 1 ) - maxf > k:
                #We are moving the left window so the element count will -
                count[s[l]] -= 1
                l+=1
                #Not decrementing maxf coz it wont make any change
            res = max(res, r - l + 1) 
        return res
        