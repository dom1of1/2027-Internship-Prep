class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0

        for num in arr1:
            for val in arr2:
                if abs(num - val) <= d:
                    break
            else:
                count += 1
        
        return count


# Time Complexity - O(n * m)
# n represents the number of elements in arr1.
# m represents the number of elements in arr2.

# Space Complexity - O(1)
