class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        pacific ocean : left and top
        atlantic ocean: right and bottom
        inputs: heights(matrix), height[r][c] -> height above sea level

        water can flow: east, west, north, south
        water can flow if neighbor <= cur cell heoght

        output: 2d grid of positions where water can flow

        approach:
        1. build list of starting cells for both the pacific and atlantic ocean
        2. Create a bfs helper that tranverses the grid inwardly (i.e. neighbor height >= current cell height)
        3. perform bfs on both pacific and atlantic ocean starters 
        4. return a list of the intersection of cells
        """
        m = len(heights)
        n = len(heights[0])
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        pacific_starts = [(0, c) for c in range(n)] + [(r, 0) for r in range(m)]
        atlantic_starts = [(m-1, c) for c in range(n)] + [(r, n-1) for r in range(m)]


        def bfs(starts):
            visited = set(starts)
            q = deque(starts)

            while q:
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                        if heights[nr][nc] >= heights[r][c]:
                            visited.add((nr, nc))
                            q.append((nr, nc))
            
            return visited


        pac = bfs(pacific_starts)
        atl = bfs(atlantic_starts)
        
        return [[r, c]  for r, c in pac & atl]





