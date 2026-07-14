
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing_type = {')':'(',']':'[','}':'{'}
        for c in s:
            if c in closing_type:
                if stack and stack[-1] == closing_type[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False                












