# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        
        dummy = ListNode(-1)   # in the case where the head node is deleted

        dummy.next = head   

        # find the length of the list
        length = 0

        curr = head

        while curr:
            curr = curr.next
            length += 1
        

        # find the n -1th node from the end and peform the deletion
        curr = dummy
        count = 0

        while curr and count < (length - n):
            curr = curr.next
            count += 1
        
        nxt = curr.next
        curr.next = nxt.next

        return dummy.next

"""
Time complexity - O(n) where n is the size of the linkedlist
Space complexity - O(1)
"""