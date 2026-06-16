class MinStack:

    def __init__(self):
        self.min = float('inf')
        self.stack = []
        

    def push(self, value: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = value
        else:
            self.stack.append(value - self.min)
            if value < self.min:
                self.min = value    
        

    def pop(self) -> None:
        if not self.stack:
            return
        pop = self.stack.pop()
        if pop < 0:
            self.min = self.min - pop    
        

    def top(self) -> int:
        top = self.stack[-1]
        if top > 0:
            return top + self.min
        else:
            return self.min    
        

    def getMin(self) -> int:
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()