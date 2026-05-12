class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1: return nums[0]
        if len(nums)==0: return 0
        sum = 0
        maxsub = nums[0]
        for i in nums:
            if sum<0:
                sum = 0
            sum +=i 
            maxsub = max(maxsub , sum)
        return maxsub   