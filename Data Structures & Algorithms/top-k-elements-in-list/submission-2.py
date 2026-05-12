class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        freq = [[] for i in range (len(nums)+1)]
        for n in nums:
            hash[n] = 1 + hash.get(n , 0)
        for n , c in hash.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq)-1,0 ,-1):
            for n in freq[i]:
                res.append(n)
                if(len(res) == k):
                    return res





        # hash = {}
        # for i in range(len(nums)):
        #     hash[nums[i]] = 1 + hash.get(nums[i] , 0)
        # n = 1
        # ans1 = list()
        # while(n<=k):
        #     ans = [key for key, val in hash.items() if val == max(hash.values())]
        #     ans1.append(ans[0])
        #     # print(hash)
        #     del hash[ans[0]]
        #     # print(ans1)
        #     # print(ans)
        #     n = n + 1
        # return (ans1)