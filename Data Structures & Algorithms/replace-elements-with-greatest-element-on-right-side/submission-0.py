class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = [0]*len(arr)
        ans[-1] = -1
        # ans[-2] = arr[-1]
        max_value = arr[-1]
        for i in range((len(arr)-2),-1,-1):
            ans[i] = max_value
            max_value = max(max_value , arr[i])
        return(ans)
