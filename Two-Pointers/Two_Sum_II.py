class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target:
                return [left + 1, right + 1]
            
            elif curr_sum > target:
                right -= 1
            
            else:
                left += 1
        
# Time Complexity - O(n)
# Use of two pointers approach here allows us to iterate through the numbers array at most once.

# Space Complexity - O(1)