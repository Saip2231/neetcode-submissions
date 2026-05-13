class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countS = {}
        for i in range(len(nums)):
            countS[nums[i]] = 1+countS.get(nums[i],0)
        max_key = max(countS, key=countS.get)
        return(max_key)