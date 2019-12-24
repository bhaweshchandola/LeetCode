class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_ele = 999999999999
        

    def push(self, x: int) -> None:
        if x<self.min_ele:
            self.min_ele = x
        return self.stack.append(x)
        
        

    def pop(self) -> None:
        del self.stack[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return sorted(self.stack)[0]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()