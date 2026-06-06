class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(1,100000):
            if i in nums:
                continue 
            else:
                return i