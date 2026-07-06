# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Space heavy but easier to maintain solution
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        curr = head

        arr = []

        while curr:
            arr.append(curr)
            curr = curr.next

        left, right = 0, len(arr) - 1

        while left < right:
            arr[left].next = arr[right]

            if left + 1 == right:
                arr[right].next = None
                break
            
            else:
                arr[right].next = arr[left + 1]

            left += 1
            right -= 1

        else:
            arr[left].next = None
            
"""
Time complexity - O(n)
Space complexity - O(n)
"""
