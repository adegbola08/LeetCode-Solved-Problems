class MinStack:

    def __init__(self):
        self.data = []
        

    def push(self, val: int) -> None:
        self.data.append(val)
        return None

    def pop(self) -> None:
        if self.data:
            self.data.pop()
        return None

    def top(self) -> int:
        if self.data:
            return self.data[-1]

    def getMin(self) -> int:
        if self.data:
            return min(self.data)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()