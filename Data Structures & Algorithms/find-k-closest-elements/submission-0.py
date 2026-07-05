class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # insertion_index = -1
        left,right = 0,len(arr)-1
        while left<=right:
            mid = (left + right)//2
            if arr[mid]<x:
                left = mid + 1
            elif arr[mid]>=x:
                right = mid -1
        idx = left
        l = idx - 1
        r = idx
        n = 0
        while (r-l-1)<k:
            if l <0:
                r+=1
            elif r == len(arr):
                l -=1
            elif abs(arr[l]-x) <= abs(arr[r]-x):
                l -= 1
            else:
                r += 1
        return arr[l+1:r]