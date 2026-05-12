class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p , s in zip(position , speed)]
        stack = []
        for p,s in sorted(pair)[::-1]:
            stack.append((target-p)/s) 
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()       
        return len(stack)
        
        
        # pair = []
        # for i in range(len(position)-1,-1,-1):
        #     # print(i)
        #     dist = ((target - position[i])/speed[i])
        #     pair.append(dist)
        #     temp = pair[0]
        #     # print(temp)
        #     # print(pair)
        #     if(dist == target):
        #         continue
        #     elif (temp > pair[-1]):
        #         pair.pop()
        #         # print(pair)
            
            
        # return (len(set(pair)))    