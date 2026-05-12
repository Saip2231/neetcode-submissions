class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        visited = set()
        q = deque()

        def check(r,c):
            if (r<0 or r == rows or c<0 or c== cols or ((r,c) in visited) or grid[r][c] == 0):
                return
            visited.add((r,c))
            q.append([r,c])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r,c])
                    visited.add((r,c))
        time = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = 2
                check(r+1,c)
                check(r-1,c)
                check(r,c+1)
                check(r,c-1)
            time +=1
        # print(grid)
        for i in range(rows):
            if 1 in grid[i]:
                return -1
        return max(0,time-1)