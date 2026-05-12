class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {'+': lambda x, y: x + y,
         '-': lambda x, y: x - y,
         '*': lambda x, y: x * y,
         '/': lambda x, y: int(x / y) if x * y >= 0 else -(-x // y)}

        for i in tokens:
            # print(i)
            if i  not in operations:
                stack.append(i)
                # print(stack)
            while(len(stack)!=0 and i in operations):
                # print(i)
                a = int(stack.pop())
                b = int(stack.pop())
                # print(stack)
                stack.append(operations[i](b,a))
                print(a,b,stack)
                i = +1
        return int(stack[0])   