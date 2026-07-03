class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        res = "".join(c for c in s if c.isalnum())

        if res == res[::-1]:
            return True
        return False