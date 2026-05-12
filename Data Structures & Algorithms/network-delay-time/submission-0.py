class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i:[] for i in range(1,(n+1))}
        for source , dest , time in times:
            adj[source].append((dest,time))

        minheap = [(0,k)]
        visited = set()
        time = 0
        while minheap:
            w1,n1  = heapq.heappop(minheap)
            if n1 in visited:
                continue
            visited.add(n1)
            time = max(time,w1)

            for n2,w2 in adj[n1]:
                if n2 not in visited:
                    heapq.heappush(minheap,(w2+w1,n2))
        return time if len(visited) == n else -1