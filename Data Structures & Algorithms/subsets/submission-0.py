class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res , sol = [],[]
        def backtrack(i):
            if i==n:
               res.append(sol[:])
               return
            backtrack(i+1) #dont pick or the left side

            sol.append(nums[i])#we pick the number of right side
            backtrack(i+1)
            sol.pop()
        backtrack(0)
        return res