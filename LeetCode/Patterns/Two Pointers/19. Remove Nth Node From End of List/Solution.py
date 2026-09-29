# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node to handle edge cases easily (e.g., removing the head node)
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        # Move right pointer n steps ahead so there is a gap of n nodes between left and right
        for _ in range(n):
            right = right.next
            
        # Move both pointers until right reaches the end of the list
        while right:
            left = left.next
            right = right.next
            
        # Delete the target node by skipping it
        left.next = left.next.next
        
        return dummy.next