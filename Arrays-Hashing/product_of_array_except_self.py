class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_mult = 1
        suffix_mult = 1
        n = len(nums)

        prefix_arr = [0] * n
        suffix_arr = [0] * n

        for i in range(n):
            j = -i - 1
            prefix_arr[i] = prefix_mult
            suffix_arr[j] = suffix_mult
            prefix_mult *= nums[i]
            suffix_mult *= nums[j]
        
        return [prefix_arr[i] * suffix_arr[i] for i in range(n)]
    

# Time Complexity - O(n)
# Space Complexity - O(n)
