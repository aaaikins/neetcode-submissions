class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visit = set()
        nRows = len(board)
        nCols = len(board[0])

        def dfs(i, row, col):
            if i == len(word):
                return True

            if (row < 0 or row >= nRows or col < 0 or col >= nCols
                    or (row, col) in visit
                    or board[row][col] != word[i]):
                return False

            # if (row, col) in visit:
            #     continue

            visit.add((row, col))
            found = (dfs(i+1, row +1, col) 
            or dfs(i+1, row, col + 1) 
            or dfs(i+1, row - 1, col)
            or dfs(i+1, row , col - 1))
            visit.remove((row, col))

            return found
        
        for r in range(nRows):
            for c in range(nCols):
                if dfs(0, r, c):
                    return True

        return False
