class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i,curr,total):
            if total == target:
                res.append(curr.copy())
                return
            if i >= len(candidates) or total>target:
                return
            curr.append(candidates[i])
            dfs(i+1,curr,total+candidates[i])
            curr.pop()
            dfs(i+1,curr,total)
        dfs(0,[],0)
        res.sort(key=lambda i:i[0])
        print(res)
        unique = [list(x) for x in set(tuple(i) for i in res)]
        return( unique)