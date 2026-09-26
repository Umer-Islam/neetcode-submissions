class Solution:

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Create 9 hash sets for each of the 3 constraint types.
        # rows[i] holds all numbers seen in Row i.
        # cols[j] holds all numbers seen in Column j.
        # boxes[k] holds all numbers seen in 3x3 Box k.
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Loop through every cell in the 9x9 grid row by row
        for r in range(9):
            for c in range(9):
                val = board[r][c]

                # Skip empty cells marked with a dot
                if val == ".":
                    continue

                # Calculate which of the nine 3x3 boxes cell (r, c) belongs to.
                # Grid row index is (r // 3) and column index is (c // 3).
                # Formula converts 2D box coordinates (0-2, 0-2) into a 1D index (0-8).
                box_idx = (r // 3) * 3 + (c // 3)

                # CHECK: Has this number appeared in the current row, column, or 3x3 box?
                if val in rows[r] or val in cols[c] or val in boxes[box_idx]:
                    return False  # Duplicate found! The Sudoku board is invalid.

                # RECORD: Save the current digit into its respective row, column, and box sets
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_idx].add(val)

        # If we checked all 81 cells without finding any duplicates, the board is valid!
        return True