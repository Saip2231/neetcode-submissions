class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prehash = {i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            prehash[crs].append(pre)
        visited = set()

        def dfs(crs):
            if crs in visited:
                return False #loop
            if prehash[crs] == []:
                return True
            
            visited.add(crs)
            for pre in prehash[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            prehash[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True