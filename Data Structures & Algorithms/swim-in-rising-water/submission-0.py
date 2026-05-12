class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows , cols = len(grid) , len(grid[0])
        minheap = [(grid[0][0],0,0)] #time,r,c
        visited = set()
        visited.add((0,0))
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        while minheap:
            time,r,c = heapq.heappop(minheap)
            if (r,c) == (rows-1 , cols-1):
                return time
            # if (r,c) in visited:
            #     continue
            # if time <= grid[r][c]:
            #     visited.add((r,c))
            # else:
            #     time +=1
            
            for dr,dc in directions:
                newr,newc = r+dr , c+dc
                if (newr<0 or newr == rows or newc<0 or newc == cols or (newr, newc) in visited):
                    continue
                visited.add((newr,newc))
                heapq.heappush(minheap,(max(time,grid[newr][newc]),newr,newc))