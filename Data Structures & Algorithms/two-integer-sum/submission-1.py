class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i,j=0,0
        for i in range(0,len(nums)):
            new = target - nums[i]
            for j in range(i+1,len(nums)):
                if ((new - nums[j]) == 0):
                    return [i,j]
        