# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if not lists:
            return None
            
        def mergeTwoLists(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
            dummy = ListNode(-1)
            tail = dummy
            while l1 and l2:
                if l1.val <= l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next
            tail.next = l1 if l1 else l2
            return dummy.next

        # Pairwise merge until one list remains
        step = 1
        n = len(lists)
        while step < n:
            for i in range(0, n - step, step * 2):
                lists[i] = mergeTwoLists(lists[i], lists[i + step])
            step *= 2
            
        return lists[0]