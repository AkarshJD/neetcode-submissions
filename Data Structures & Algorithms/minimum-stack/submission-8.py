class MinStack:
    def __init__(self):
        self.stack = []
        self.minElement = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minElement[-1] if self.minElement else val)
        self.minElement.append(val)
    def pop(self) -> None:
        self.stack.pop()
        self.minElement.pop()

    def top(self) -> int:
        return(self.stack[-1])

    def getMin(self) -> int:
        return(self.minElement[-1])
