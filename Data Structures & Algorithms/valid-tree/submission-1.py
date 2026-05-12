class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        visited = set()
        adjlist = {i:[] for i in range(n)}
        for node1,node2 in edges:
            adjlist[node1].append(node2)
            adjlist[node2].append(node1)
        # print(adjlist)

        def dfs(cur ,prev):
            if cur in visited:
                return False 
            visited.add(cur)
            for j in adjlist[cur]:
                if j == prev:
                    continue
                if not dfs(j,cur):
                    return False
            return True
        
        return dfs(0,-1) and n == len(visited)
        
