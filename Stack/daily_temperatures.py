class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # create our answer output initialized to 0 for each position
        # no of days = index of greater - current index
        # create our monotonic stack
        # for each element in temperatures, while our stack is non-empty and the current temp is greater than what's on top of stack, 
        # pop top of stack, calculate days using index. 
        # Add days to answer using stack element's index and append tuple (index, curr_temperature) to stack
        
        stack = []
        answer = [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                prev_idx, prev_temp = stack.pop()
                answer[prev_idx] = idx - prev_idx
            
            stack.append((idx, temp))
        
        return answer


# for an even more optimal solution, we could do this using just the indices without creating the tuples
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        answer = [0] * n
        
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                answer[idx] = i - idx
            
            stack.append(i)
        
        return answer


"""
Time Complexity - O(n)
We iterate through nums2 once. Each element is pushed onto the stack at
most once and popped from the stack at most once, so the total work is
O(n) (iteration) + O(n) (pushes) + O(n) (pops) = O(n).

Space Complexity - O(n)
We create an answer list and a stack, each of which can store
at most n elements.
"""