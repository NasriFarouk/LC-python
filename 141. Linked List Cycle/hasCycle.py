# Definition for singly-linked list.
class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next = None

class Solution:
        def hasCycle(self, head: ListNode) -> bool:
            # the logic is to use two pointers, slow and fast
            # slow pointer will move one step at a time
            # fast pointer will move two steps at a time
            # if there is a cycle, the slow and fast pointers will meet at some point
            # if there is no cycle, the fast pointer will reach the end of the linked list
            # this way, we can check if the linked list has a cycle in linear time
            # and constant space
            if head is None:
                return False
            slow = head
            fast = head.next
            while slow != fast:
                if fast is None or fast.next is None:
                    return False
                slow = slow.next
                fast = fast.next.next
            return True


    def hasCycleBruteForce(self, head: ListNode) -> bool:
        # the logic is to use a set to store the nodes we have seen
        # if we see a node again, we return True
        # if we reach the end of the linked list, we return False
        # this way, we can check if the linked list has a cycle in linear time
        # and constant space
        nodeSet = set()
        while head:
            if head in nodeSet :
                return True
            nodeSet.add(head)
            head = head.next
        return False 
        