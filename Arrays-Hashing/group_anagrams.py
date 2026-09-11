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
Time Complexity - O(n * k)
We iterate through each string to create the count list after iterating through the strings array.

Space Complexity - O(n * k)
The hashmap stores n strings, each up to k characters, so it uses O(n * k) space.
The 26-element count tuple is O(1) per key since the alphabet size is fixed.
The output also requires O(n * k) space.
Overall: O(n * k).

n - number of strings in the input array
k - maximum length of a string in the array
'''

# another approach (Less efficient)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag_Map = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            anag_Map[key].append(s)
        
        return list(anag_Map.values())

'''
Time Complexity - O(n × k × log k)
For each of the n strings, we perform a sorting operation using sorted(s)
Sorting a string of length k takes O(k × log k) time
Therefore, the total time complexity is O(n × k × log k)

Space Complexity - O(n × k)
The dictionary stores all n strings, where each string has up to k characters, requiring O(n × k) space
For each string, we create a sorted key string which takes O(k) space temporarily
The output list contains all the original strings, which is O(n × k) space
Overall space complexity is O(n × k)

n is the number of strings in the input array
k is the maximum length of a string in the array
'''