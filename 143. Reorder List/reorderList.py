Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        # the logic is to use two pointers, slow and fast
        # we will iterate through the linked list with the slow pointer
        # we will move the fast pointer to the end of the linked list
        # we will then reverse the second half of the linked list
        # we will then merge the two halves of the linked list
        if not head :
            return
        
        slow = fast = head
        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        current = slow
        while current :
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        

        first = head
        second = prev
        while second.next :
            nextFirstNode = first.next
            first.next = second
            first = nextFirstNode

            nextSecondNode = second.next
            second.next = first
            second = nextSecondNode
        