class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find min index (index of minimum value)
        # if min index is 0, perform binary search with normal boundaries
        # otherwise, check range that target falls in 
        # Perform binary search in the range
        
        n = len(nums)

        if n == 1:
            return 0 if nums[0] == target else -1     #Edge case for single value nums array

        #finding min index
        l, r = 0, n - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            
            else:
                r = mid
        
        min_index = l

        def binary_search(l, r):
            while l <= r:
                mid = (l + r) // 2

                if nums[mid] == target:
                    return mid
                
                elif nums[mid] > target:
                    r = mid - 1
                
                else:
                    l = mid + 1
            
            return -1
                

        if min_index == 0:
            return binary_search(0, n - 1)

        elif target >= nums[0] and target <= nums[min_index - 1]:
            return binary_search(0, min_index - 1)
        
        else:
            return binary_search(min_index, n - 1)

# Time Complexity - O(log n)
# Space Complexity - O(1)