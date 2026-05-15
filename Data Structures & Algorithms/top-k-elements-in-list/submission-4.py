class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countS = {}
        freq = [[]for i in range(len(nums)+1)]
        for i in range(len(nums)):
            countS[nums[i]] = 1 + countS.get(nums[i],0)
        for n,c in countS.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq)-1 , 0,-1):
            for n in freq[i]:
                res.append(n)
            if len(res) == k:
                break;
        return res