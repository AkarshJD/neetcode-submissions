class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s)).lower()
        head = 0
        tail = len(s)-1
        for i in range(len(s)):
            if(s[head] == s[tail]):
                head+=1
                tail-=1
            else:
                return False
        return True