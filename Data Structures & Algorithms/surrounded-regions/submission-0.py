class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        def dfs(i, j):
            if (i < 0 or i >= m) or (j < 0 or j >= n) or board[i][j] != 'O':
                return 
            
            board[i][j] = 'T'

            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i - 1, j)
            dfs(i, j - 1)
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O' and (r in [0, m - 1] or c in [0, n - 1]):
                    dfs(r, c)

        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'
                

        