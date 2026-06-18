class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for ch in s:
            inside = ''
            num = ''
            if ch == ']':
                while stack[-1]!= '[':
                    a = stack.pop()
                    inside+=a
                inside = inside[::-1]
                print(inside)
                stack.pop()
                while stack and stack[-1].isdigit():
                    b = stack.pop()
                    num += b
                    print(num)
                num = num[::-1]
                stack.extend(inside * int(num))
            else:
                stack.append(ch)
        return (''.join(stack))