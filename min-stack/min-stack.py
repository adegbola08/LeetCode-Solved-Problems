class MinStack(object):

    def __init__(self):
        self.lst = []

    def push(self, val):
        self.lst.append(val)
        

    def pop(self):
        if self.lst:
            self.lst.pop()
        

    def top(self):
        if self.lst:
            return self.lst[-1]
        
    def getMin(self):
        if self.lst:
            return min(self.lst)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()