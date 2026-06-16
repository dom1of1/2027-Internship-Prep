class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        result = []

        for index, num in enumerate(nums):
            if num > 0:
                break
            
            if index > 0 and num == nums[index - 1]:
                continue

            left, right = index + 1, len(nums) - 1

            while left < right:
                three_sum = num + nums[left] + nums[right]

                if three_sum > 0:
                    right -= 1
                
                elif three_sum < 0:
                    left += 1
                
                else:
                    result.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        
        return result
                    

# Time Complexity - O(n^2)
# Space Complexity - O(1)