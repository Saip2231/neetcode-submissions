class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def ispossible(nums,k,maxallowed):
            inital = 1
            val = 0
            for i in range(0,len(nums)):
                if (val + nums[i]) <= maxallowed:
                    val+=nums[i]
                else:
                    inital+=1
                    val = nums[i]
            
            if inital<=k:
                return True
            else:
                return False

        start = max(nums)
        end = sum(nums)
        ans = -1
        while start <= end:
            mid = (start + (end - start)//2)
            if ispossible(nums , k,mid):
                ans = mid
                end = mid-1
            else:
                start = mid + 1
        return ans