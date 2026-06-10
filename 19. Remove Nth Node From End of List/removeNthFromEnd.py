# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # the logic is to use two pointers, first and second
        # we will iterate through the linked list with the first pointer
        # we will move the second pointer to the nth node from the end
        # we will then move the first and second pointers to the next node
        # we will then remove the nth node from the end
        # we will return the head of the linked list
        dummy= ListNode(0)
        dummy.next = head
        first=dummy
        second=dummy
        for i in range(n+1):
            first = first.next
        while first :
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next
        