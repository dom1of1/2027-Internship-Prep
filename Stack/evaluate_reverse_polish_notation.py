class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # keep adding numbers to stack till we meet an operator
        # retrieve last two numbers in the stack, perform operation and add result to stack
        # check order of operation for subtraction and division since they aren't commutative
        # return final element in stack
        
        stack = []

        for char in tokens:            
            if char in "+-*/":
                num1 = stack.pop()
                num2 = stack.pop()

                if char == "+":
                    stack.append(num1 + num2)
                
                elif char == "-":
                    stack.append(num2 - num1) 
                
                elif char == "*":
                    stack.append(num1 * num2)
                
                else:
                    stack.append(int(num2 / num1)) #discarding decimal part to truncate towards zero
            
            else:
                stack.append(int(char))

        return stack[0]

"""
Time complexity - O(n) 
We iterate through the tokens list once.

Space complexity: O(n)
In the worst case, we push many operands before encountering any operators, so the stack can hold up to n elements, where n is the number of input tokens
"""