class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #validate each row
        for row in board:
            distinct = set()
            for num in row:
                if num == ".":
                    continue
                
                if num not in distinct:
                    distinct.add(num)
                
                else:
                    return False
 
        #validate each col
        for i in range(9):
            col = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue

                if board[j][i] not in col:
                    col.add(board[j][i])
                
                else:
                    return False

        # helper function for sub-grid check
        def valid_grid(r,c):
            box = set()
            for row in range(r, r+3):
                for col in range(c, c+3):
                    if board[row][col] == ".":
                        continue

                    if board[row][col] not in box:
                        box.add(board[row][col])
                
                    else:
                        return False
            
            return True


        # validate each sub-box
        for i in range(0, 9 , 3):
            for j in range(0, 9, 3):  #getting the starting coordinates for each sub box
                if not(valid_grid(i, j)):
                    return False
                
        return True

"""
Time Complexity - O(1)
The input size never changes because a Sudoku board is always 9×9.
We always perform the same number of operations:
- 81 checks for rows
- 81 checks for columns
- 81 checks for 3×3 sub-boxes
Total ≈ 243 fixed operations, so runtime does not scale with input size.

Space Complexity - O(1)
The space usage is constant because at any point in execution we only store a constant number of small sets (row, column, or box checks), and each set can hold at most 9 elements (digits 1–9).
Although new sets are created during different phases of the algorithm, they are not all stored at the same time. Previous sets become unreachable after each iteration and are discarded, so memory does not accumulate over time.
"""