class Solution:
    def isValid(self, s: str) -> bool:

        # create a bracket Map
        # add open brackets to our stack till we see a closed bracket
        # at closed, check if stack isn't empty and that we found the correct closed bracket for the open bracket currently on top of the stack.
        # if yes, pop open bracket. No, return False
        # check if stack is empty after iteration.

        bracket_Map = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }

        stack = []
        for char in s:
            if char in bracket_Map:
                stack.append(char)

            else:
                if stack and (char == bracket_Map[stack[-1]]):
                    stack.pop() 
                       
                else:
                    return False
        
        return len(stack) == 0

"""
Time complexity - O(n)
Space complexity - O(n) - worst case where we have all open brackets in the input string.
"""