class Solution:

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # 1. Check all rows
        for r in range(9):
            seen = set()
            for c in range(9):
                val = board[r][c]
                if val != '.':
                    if val in seen:
                        return False
                    seen.add(val)

        # 2. Check all columns
        for c in range(9):
            seen = set()
            for r in range(9):
                val = board[r][c]
                if val != '.':
                    if val in seen:
                        return False
                    seen.add(val)

        # 3. Check all nine 3x3 boxes
        for box_row in range(3):
            for box_col in range(3):
                seen = set()
                for r in range(3):
                    for c in range(3):
                        val = board[box_row * 3 + r][box_col * 3 + c]
                        if val != '.':
                            if val in seen:
                                return False
                            seen.add(val)

        return True