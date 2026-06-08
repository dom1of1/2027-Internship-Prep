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
# The nested while loop only runs when num - 1 is not in the set hence it does not become O(n^2) as one might suspect.

# Space Complexity - O(n)