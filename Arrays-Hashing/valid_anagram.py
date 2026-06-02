class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        letters = {}

        for char in s:
            if char in letters:
                letters[char] += 1
            
            else:
                letters[char] = 1
        
        for char in t:
            if char not in letters:
                return False
            
            else:
                letters[char] -= 1
                if letters[char] == 0:
                    del letters[char]
        
        return True if len(letters) == 0 else False
        