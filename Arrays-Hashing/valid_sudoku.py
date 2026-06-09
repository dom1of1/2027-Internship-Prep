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

# Time Complexity - O(1) (fixed 9×9 board)
# Space Complexity - O(1) (bounded sets)