class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_count = [0] * 26
        for char_s, char_t in zip(s,t):
            char_count[ord(char_s) - ord('a')] += 1
            char_count[ord(char_t) - ord('a')] -= 1
        
        if(all(count == 0 for count in char_count)):
            return True
        return False