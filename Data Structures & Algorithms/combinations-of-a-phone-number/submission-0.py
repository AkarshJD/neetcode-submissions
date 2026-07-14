class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitsToChar = {  "2": "abc",
                    "3": "def",
                    "4": "ghi",
                    "5": "jkl",
                    "6": "mno",
                    "7": "pqrs",
                    "8": "tuv",
                    "9": "wxyz" }

        def backtrack( i, curStr):
            #base case
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            
            #Recurcise call
            for c in digitsToChar[digits[i]]:
                backtrack(i + 1, curStr + c)

        if digits:
            #Coz it will go inside and return [""]
            backtrack(0, "")

        return res