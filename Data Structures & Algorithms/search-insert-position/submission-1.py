class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def search_mid(start,end):
            return ((start+end)//2)

        start,end = 0 ,len(nums)-1
        while start<=end:
            mid = search_mid(start,end)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid -1
            else:
                start = mid +1
            # print(mid)
        return start
        # print(mid+1)
