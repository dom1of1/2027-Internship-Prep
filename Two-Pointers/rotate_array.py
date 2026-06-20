#Brute Force Solution
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        result = [0] * len(nums)

        for index, num in enumerate(nums):
            new_idx = (index + k) % len(nums)
            result[new_idx] = num
        
        nums[:] = result

# Time Complexity - O(n)
# Space Complexity - O(n)



#Optimal Solution
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums.reverse()

        l, r = 0, k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        
        
        l, r = k, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

# Time Complexity - O(n)
# Space Complexity - O(1)