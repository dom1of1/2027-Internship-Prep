class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #(index, height)
        max_area = 0

        for i, height in enumerate(heights):
            start = i 

            while stack and height < stack[-1][1]:
                j, h = stack.pop()
                width = i - j
                area = h * width
                max_area = max(max_area, area)
                start = j #current histogram extends backwards
            
            stack.append((start, height))
        
        while stack:
            j, h = stack.pop()
            width = len(heights) - j
            area = h * width
            max_area = max(max_area, area)
        
        return max_area

"""
Time complexity - O(n) - Each element is pushed onto the stack at most once and popped at most once.

Space complexity - O(n) - worst case where stack could store n elements(equivalent to the size of the heights).
"""