class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {i:[] for i in range(N)}
        for i in range(N):
            x1,y1 = points[i]    
            for j in range(i+1,N):
                x2,y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)   
                adj[i].append([dist,j]) 
                adj[j].append([dist,i]) 
        # print(adj)
       
        
        visited = set()
        result = 0
        minheap = [[0,0]]
        while len(visited) < N:
            cost , i = heapq.heappop(minheap)
            if i in visited:
                continue
            result = result + cost 
            visited.add(i)
            for neicost , nei in adj[i]:
                if nei not in visited:
                    heapq.heappush(minheap , [neicost,nei])
        
        return result
