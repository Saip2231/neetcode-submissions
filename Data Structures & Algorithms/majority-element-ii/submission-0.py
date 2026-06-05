class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
        print(freq)
        limit = len(nums)//3
        res = [num for num, cnt in freq.items() if cnt > limit]
        return res