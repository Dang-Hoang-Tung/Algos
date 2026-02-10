from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows: dict[int, set[str]] = defaultdict(set)
        cols: dict[int, set[str]] = defaultdict(set)
        areas: dict[tuple[int, int], set[str]] = defaultdict(set)

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue

                area = (i // 3, j // 3)
                if val in rows[i] or val in cols[j] or val in areas[area]:
                    return False
                
                rows[i].add(val)
                cols[j].add(val)
                areas[area].add(val)

        return True
