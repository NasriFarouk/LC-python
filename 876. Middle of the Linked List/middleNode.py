# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # the logic is to use two pointers, fast and slow
        # fast pointer will move two steps at a time
        # slow pointer will move one step at a time
        # when fast pointer reaches the end of the linked list, slow pointer will be at the middle of the linked list
        # this way, we can return the middle node of the linked list in linear time
        # and constant space
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def middleNodeBruteForce(self, head: ListNode) -> ListNode:
        # the logic is to count the total number of nodes in the linked list
        # and then we walk to the middle index
        # the middle index is the count // 2
        # if the count is odd, we return the exact middle
        # if the count is even, we return the second middle
        # this way, we can return the middle node of the linked list in linear time
        # and constant space
        count = 0
        current = head
        while current:
            count += 1
            current = current.next

        steps = count // 2

        node = head
        while steps > 0:
            node = node.next
            steps -= 1

        return node