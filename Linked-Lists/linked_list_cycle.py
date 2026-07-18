# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        sett = set()

        curr = head

        while curr:
            if curr in sett:
                return True
            
            else:
                sett.add(curr)

            curr = curr.next

        return False

# Time Complexity - O(n)
# Space Complexity - O(n)


#Optimal Solution (Floyd's Tortoise and Hare Algorithm)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
                
        return False

"""
Time complexity - O(n) 
Space complexity - O(1)
"""
