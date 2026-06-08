class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)

        longest = 0

        for num in sett:
            if num - 1 not in sett:
                length = 1
                next_num = num + 1

                while next_num in sett:
                    length += 1
                    next_num += 1
            
                longest = max(length, longest)

        return longest

# Time Complexity - O(n)
# Space Complexity - O(n)