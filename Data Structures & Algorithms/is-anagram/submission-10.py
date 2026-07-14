# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False

#         #BUilding the HM
#         countS, countT = {}, {}

#         for i in range(len(s)):
#             countS[s[i]] = 1 + countS.get(s[i], 0) 
#             countT[t[i]] = 1 + countT.get(t[i], 0)

#         #Iterate through them
#         for c in countS:
#             if countS[c] != countT.get(c,0):
#                 return False
#         return True



class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """An anagram is a string that contains the exact same 
        characters as another string, 
        but the order of the characters can be different."""

        """
        1. build a hash map
        2. add items to hashmap for the length of the string one for each with counts
        3. while counting the elements and adding them

        4. iterate over one of them
        5. check if that element's count doesnt matche the other element's count
        6. return false if it does not match
        7. return true if it matches
        """
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        # if it doesnt exist it just replaces by 0
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) 
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for i in countS:
            if countS[i] != countT.get(i,0):
                return False
        return True



