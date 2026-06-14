class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = list()
        for i in range(0,len(nums)):
            if(i>0 and nums[i] == nums[i-1]):
                continue
            for j in range(i+1,len(nums)):
                if j>i+1 and nums[j] == nums[j-1]:
                    continue
                p,q = j+1 , len(nums)-1
                while(p<q):
                    sum = nums[i] + nums[j] + nums[p] + nums[q]
                    if sum < target:
                        p+=1
                    elif sum > target:
                        q-=1
                    else:
                        ans.append([nums[i] , nums[j],nums[p],nums[q]])
                        p+=1
                        q-=1
                        while(p<q and nums[p] == nums[p-1]):
                            p+=1
                        while (p<q and nums[q] == nums[q+1]):
                            q-=1
        return (ans)