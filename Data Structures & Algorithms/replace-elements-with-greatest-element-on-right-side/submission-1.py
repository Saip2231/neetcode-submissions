class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_value = -1
        for i in range((len(arr)-1),-1,-1):
            new_max = max(arr[i] , max_value)
            arr[i] = max_value
            max_value = new_max
        return(arr)
