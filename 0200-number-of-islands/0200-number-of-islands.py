# BFS : group 찾기 (not visited)
# by connecting adjacent lands horizontally or vertically
cases = [(0,1), (1,0), (0, -1), (-1, 0)]

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # n x m
        n = len(grid)
        m = len(grid[0])

        def bfs(x:int, y:int):

            grid[x][y] = "0"

            for dx, dy in cases:
                if 0 <= x+dx < n and 0 <= y+dy < m and grid[x+dx][y+dy] =="1":
                    bfs(x+dx, y+dy)

        cnt = 0
        for x in range(n):
            for y in range(m):
                if grid[x][y]=="1":
                    bfs(x, y)
                    cnt += 1

        return cnt