class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        def f(arr,n,target):
            low ,high= 0,n-1
            while(low<=high):
                mid = low + (high - low)//2
                if arr[mid] == target:
                    return True
                elif arr[mid] == arr[low] and arr[mid] == arr[high]: 
                    low = low + 1
                    high = high - 1
                    continue 
                if arr[low]<=arr[mid]:
                    if(arr[low]<=target and target<=arr[mid]):
                        high = mid-1
                    else:
                        low = mid+1 
                else:
                    if(arr[mid]<=target and target <= arr[high]):
                        low = mid + 1
                    else:
                        high = mid-1
            return False

        arr = nums
        n = len(nums)
        return(f(arr,n,target))