class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()
        for i in triplets:
            if i[0]>target[0] or i[1]>target[1] or i[2]>target[2]:
                continue
            for j,v in enumerate(i):
                if v == target[j]:
                    good.add(j)
        if len(good)==3:
            return True
        else:
            return False