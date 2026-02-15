class Solution:
    def searchRow(self, rows: list[list[int]], target: int) -> list[int]:
        if len(rows) == 0:
            return []
        if len(rows) == 1:
            return rows[0]

        mid = (len(rows)-1) // 2
        
        if rows[mid][0] <= target and rows[mid][-1] >= target:
            return rows[mid]
        elif rows[mid][0] > target:
            return self.searchRow(rows[:mid], target)
        else:
            return self.searchRow(rows[mid+1:], target)
        
    def searchNum(self, row: list[int], target: int) -> bool:
        if len(row) == 0:
            return False
        mid = len(row) // 2
        if row[mid] == target:
            return True
        if row[mid] > target:
            return self.searchNum(row[:mid], target)
        if row[mid] < target:
            return self.searchNum(row[mid+1:], target)
        return False

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        row = self.searchRow(matrix, target)
        result = self.searchNum(row, target)
        return result
    