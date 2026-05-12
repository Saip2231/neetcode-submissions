class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left , right = 0,len(nums)-1
        ans = list()
        while(left<right):
            if (nums[left]+ nums[right] == target):
                ans.append(left+1)
                ans.append(right+1)
                return ans
            if (nums[left] + nums[right] > target):
                right = right -1
            if(nums[left] + nums[right] < target):
                left = left +1
        return ans