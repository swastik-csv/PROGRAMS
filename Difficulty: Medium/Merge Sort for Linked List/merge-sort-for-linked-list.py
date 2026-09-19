''' Structure of a Linked List node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def mergeSort(self, head):
        # Base case
        if head is None or head.next is None:
            return head

        # Find the middle of the linked list
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Split into two halves
        mid = slow.next
        slow.next = None

        # Sort both halves
        left = self.mergeSort(head)
        right = self.mergeSort(mid)

        # Merge the sorted halves
        return self.merge(left, right)

    def merge(self, left, right):
        dummy = Node(0)
        tail = dummy

        while left and right:
            if left.data <= right.data:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next

            tail = tail.next

        # Attach remaining nodes
        if left:
            tail.next = left
        else:
            tail.next = right

        return dummy.next