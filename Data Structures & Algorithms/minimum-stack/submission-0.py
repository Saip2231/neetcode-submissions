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


    
# if __name__ == '__main__':
#     stack = MinStack()
# ans = list()
# inn = ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]
# for i in range(0 , len(inn)):
#     if inn[i] == "push":
#         ans.append(stack.push(inn[i+1]))
#     if inn[i] == 'pop':
#         ans.append(stack.pop())
#     if inn[i] == 'getMin':
#         ans.append(stack.getMin())
#     if inn[i] == 'top':
#         ans.append(stack.top())
#     print(ans)
# print(stack.top())
        
    
    
    
    