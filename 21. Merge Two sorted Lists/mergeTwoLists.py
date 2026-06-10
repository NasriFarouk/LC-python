# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # the logic is to use two pointers, l1 and l2
        # we will iterate through the two lists and compare the values of the nodes
        # we will add the smaller value node to the new list
        # we will move the pointer of the list with the smaller value node to the next node
        # we will continue this process until we reach the end of one of the lists
        # then, we will add the remaining nodes of the other list to the new list
        # we will return the new list

        # maintain an unchanging reference to node ahead of the return node.
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        # At least one of l1 and l2 can still have nodes at this point, so connect
        # the non-null list to the end of the merged list.
        prev.next = l1 if l1 is not None else l2

        return prehead.next
