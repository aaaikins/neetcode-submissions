class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dict = defaultdict(set)
        col_dict = defaultdict(set)
        sub_matrix = defaultdict(set)

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                if val in row_dict[i]:
                    return False
                row_dict[i].add(val)
                if val in col_dict[j]:
                    return False
                col_dict[j].add(val)

                mat_idx = (i//3) * 3 + (j//3)
                if val in sub_matrix[mat_idx]:
                    return False
                sub_matrix[mat_idx].add(val)
        return True
                