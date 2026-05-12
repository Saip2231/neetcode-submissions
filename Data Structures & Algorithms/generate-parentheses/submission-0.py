class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # if n == 0:
        #     return ans
        # if n==1:
        #     ans.append('()') 
        #     return ans

        stack = []
        res = []
        def backtracking(openN , closedN):
            if openN == closedN == n:
                res.append(''.join(stack))
                return 
            
            if openN < n:
                stack.append('(')
                backtracking(openN+1 , closedN)
                stack.pop()

            if closedN < openN:
                stack.append(')')
                backtracking(openN , closedN+1)
                stack.pop()

        backtracking(0,0) 
        return res

