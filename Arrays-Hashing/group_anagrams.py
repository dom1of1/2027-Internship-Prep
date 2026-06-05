from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_map = defaultdict(list)

        for string in strs:
            count = [0] * 26
            
            for char in string:
                count[ord(char) - ord('a')] += 1
            
            key = tuple(count)

            anagrams_map[key].append(string)
        
        return list(anagrams_map.values())
        


'''

   Time Complexity - O(n * m)
   Space Complexity - O(n * m)
   n - number of strings
   m - length of each string

'''

