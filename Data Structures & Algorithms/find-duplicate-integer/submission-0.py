class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hash = {}
        for i in range(len(nums)):
            hash[nums[i]] = 1 + hash.get(nums[i] , 0)
        print(hash)
        ans = [key for key, val in hash.items() if val ==  max(hash.values())]
        return (ans[0])