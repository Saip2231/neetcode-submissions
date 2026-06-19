class MinStack:
    def __init__(self):
        self.s = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.s.append(val)
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)
        else:
            self.minStack.append(self.minStack[-1])

    def pop(self) -> None:
        if self.s:
            self.s.pop()
            self.minStack.pop()

    def top(self) -> int:
        return self.s[-1] if self.s else -1

    def getMin(self) -> int:
        return self.minStack[-1] if self.minStack else -1


    

        
    
    
    
    