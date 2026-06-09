# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # the logic is to iterate through the linked list while always keeping track of the previous node
        # and the next node . the we change the direction of each node by pointing his next to the previous node
        # and then we move the previous node to the current node and the current node to the next node
        # and we continue this process until we reach the end of the linked list
        # at the end, we return the previous node since he is pointing at the last element of the original linked list
        current = head
        previous = None
        while current :
            nextNode = current.next
            current.next=previous
            previous=current
            current=nextNode
        return previous