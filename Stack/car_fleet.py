class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p,s) for p,s in zip(position,speed)]

        stack = []

        for p, s in sorted(pairs)[::-1]:
            time_taken = (target - p) / s
            stack.append(time_taken)

            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)

"""
Time complexity - O(n log n). The time used for sorting dominates the O(n) traversal of the sorted pairs list.

Space complexity - O(n). The pairs list stores n elements. In the worst case, every car forms its own fleet, so the stack also stores n elements.
"""