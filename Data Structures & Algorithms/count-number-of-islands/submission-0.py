class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        import collections

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        count = 0

        def bfs(start_r, start_c):
            q = collections.deque()
            q.append((start_r, start_c))
            visited.add((start_r, start_c))

            while q:
                r0, c0 = q.popleft()
                for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                    r, c = r0 + dr, c0 + dc
                    if 0 <= r < rows and 0 <= c < cols:
                        if grid[r][c] == '1' and (r, c) not in visited:
                            visited.add((r, c))
                            q.append((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r, c)
                    count += 1

        return count
