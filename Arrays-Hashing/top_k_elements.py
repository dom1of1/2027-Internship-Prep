from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_Map = defaultdict(int)

        for num in nums:
            num_Map[num] += 1

        pairs = list(num_Map.items())  
        pairs.sort(key = lambda x:x[1], reverse = True) 

        result = [pair[0] for pair in pairs[:k]] 
        
        return result
    

# Time Complexity - O(n log n)
# Space Complexity - O(n)