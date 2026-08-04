from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[set() for _ in range(9)]
        col=[set() for _ in range(9)]
        boxes=[set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    continue
                nums=board[i][j]
                box=(i//3)*3+(j//3)
                if nums in rows[i] or nums in col[j] or nums in boxes[box]:
                    return False
                rows[i].add(nums)
                col[j].add(nums)
                boxes[box].add(nums)
        return True
        

        