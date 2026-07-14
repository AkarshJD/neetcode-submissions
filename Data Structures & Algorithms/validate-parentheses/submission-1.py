class Stack:
    def __init__(self):
        self.stack = []
    
    # Push method to add an element to the stack
    def push(self, value):
        self.stack.append(value)
    
    # Pop method to remove and return the top element
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty!")
            return None
    
    # Peek method to view the top element without removing it
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty!")
            return None
    
    # Check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0
    
    # Return the size of the stack
    def size(self):
        return len(self.stack)

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












