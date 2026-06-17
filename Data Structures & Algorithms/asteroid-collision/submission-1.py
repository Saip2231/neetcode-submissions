class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in range(len(asteroids)):
            if asteroids[i]>0:
                stack.append(asteroids[i])
            else:
                while(
                    len(stack)!=0 
                    and stack[-1]>0 
                    and stack[-1]<abs(asteroids[i])
                    ):
                    stack.pop()
                if (len(stack)!=0 and stack[-1] == abs(asteroids[i])):
                    stack.pop()
                elif (len(stack)==0 or stack[-1]<0):
                    stack.append(asteroids[i])
        return(stack)