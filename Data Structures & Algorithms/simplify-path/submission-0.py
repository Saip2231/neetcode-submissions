class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        # stack.append('/')
        arr = path.split('/')
        arr = list(filter(lambda x: x != '', arr))
        print(arr)
        for ch in arr:
            if stack and ch == '..':
                stack.pop()
                continue
            else: 
                if ch and (ch!= '..' and ch!='.'):
                    stack.append(ch)
        ans = '/'.join(stack)
        ans = '/' + ans
        return(ans)