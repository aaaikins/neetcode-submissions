from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        nRows = len(grid)
        nCols = len(grid[0])
        q = deque([])
        fresh = 0

        for r in range(nRows):
            for c in range(nCols):
                cur_time = 0
                if grid[r][c] == 2:
                    q.append((r, c, 0))
                elif grid[r][c] == 1:
                    fresh += 1


        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        time = 0
        while q:
            r, c, t = q.popleft()
            time = max(time, t)
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < nRows) and (0<= nc < nCols) and (grid[nr][nc] == 1):
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc, t + 1))

        return time if fresh == 0 else -1




                

        return total_time
        