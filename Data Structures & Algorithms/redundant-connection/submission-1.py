class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        def dfs(src,target,visited):
            if src == target:
                return True
            visited.add(src)
            for nei in graph[src]:
                if nei not in visited:
                    if dfs(nei,target,visited):
                        return True
            return False
        for u,v in edges:
            visited = set()
            if u in graph and v in graph and dfs(u,v,visited):
                return [u,v]

            graph[u].append(v)
            graph[v].append(u)
        return []