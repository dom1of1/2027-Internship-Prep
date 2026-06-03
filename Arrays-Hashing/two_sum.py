class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_Map = {}

        for index, num in enumerate(nums):
            remainder = target - num
            if remainder in num_Map:
                return [index, num_Map[remainder]]
            
            else:
                num_Map[num] = index