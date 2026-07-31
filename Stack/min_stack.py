# Approach 1 (attaching current min to new values in a tuple form when pushing)
# Found this to be more intuitive tbh.
class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, value: int) -> None:
        if self.stack:
            self.minn = min(value, self.stack[-1][1]) 
        else:
            self.minn = value
        
        self.stack.append((value, self.minn))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

# Approach 2 (Using a min stack to keep track of current min)
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


"""
For both approaches 
Time complexity - O(1)
Space complexity - O(n) - for the push method, self.stack increases/grows linearly with respect to input size.
"""