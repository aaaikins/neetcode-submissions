class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.minVal:
            self.minVal = val
        

    def pop(self) -> None:
        self.stack.pop()
        if self.stack:
            self.minVal = min(set(self.stack))
        else:
            self.minVal = float('inf')
         
        

    def top(self) -> int:
        return self.stack[-1]  

    def getMin(self) -> int:
        return self.minVal
        
