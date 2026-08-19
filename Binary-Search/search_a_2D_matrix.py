
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Intuition
        # We can assume the elements are in an array and perform normal binary search.
        # The key difference here though is that when we find the mid index, since it's a matrix we can't use that index directly to access the mid element. We have to find the row idx and col idx.
        # However, we can compute these using the original mid index.
        # row index = mid index // num of cols
        # col index = mid index % num of cols
        # now, the rest of the algorithm is pretty easy. Just the usual binary search.

        rows, cols = len(matrix), len(matrix[0])

        left, right = 0, (rows * cols) - 1


        while left <= right:
            mid = (left + right) // 2

            row_idx = mid // cols
            col_idx = mid % cols

            if matrix[row_idx][col_idx] == target:
                return True
            
            elif matrix[row_idx][col_idx] > target:
                right = mid - 1
            
            else:
                left = mid + 1
        
        return False

# Time complexity - O(log(n*m))
# Space complexity - O(1)