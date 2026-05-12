class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {'+': lambda x, y: x + y,
         '-': lambda x, y: x - y,
         '*': lambda x, y: x * y,
         '/': lambda x, y: int(x / y) if x * y >= 0 else -(-x // y)}

        for token in tokens:
            if token not in operations:
                stack.append(int(token))
            else:
                a = stack.pop()
                b = stack.pop()
                stack.append(operations[token](b, a))
        return int(stack[0])   