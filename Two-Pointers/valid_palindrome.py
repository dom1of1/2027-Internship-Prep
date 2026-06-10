class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        
        lower_s = s.lower()

        i, j = 0, len(lower_s) - 1

        while i < j:
            while i < j and not lower_s[i].isalnum():
                i += 1

            while i < j and not lower_s[j].isalnum():
                j -= 1

            if lower_s[i] != lower_s[j]:
                return False

            i += 1
            j -= 1

        return True

# Time Complexity - O(n)
# Space Complexity - O(n)