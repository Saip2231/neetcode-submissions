class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = list()
        
        for i , a in enumerate(nums):
            if(i>0 and a == nums[i-1]):
                continue
            
            j,k = i+1 , len(nums)-1
            while(j<k):
                print(a , nums[j] , nums[k])
                if(a + nums[j]+nums[k]>0):
                    k = k-1
                elif(a + nums[j] + nums[k]<0):
                    j = j+1
                else:
                    ans.append([a,nums[j],nums[k]])
                    
                    j = j+1
                    while(nums[j] == nums[j-1] and j<k):
                        j = j+1
        return (ans) 