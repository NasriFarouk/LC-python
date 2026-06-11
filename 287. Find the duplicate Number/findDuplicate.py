class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # the logic is to treat this problem as linked list and finding the loop ( the duplicate number )
        # we use two pointers, slow and fast
        # slow pointer will move one step at a time
        # fast pointer will move two steps at a time
        # if there is a cycle, the slow and fast pointers will meet at some point
        # then for some reason if we reset slow, they will meet at the duplicate number
        # this way, we can find the duplicate number in linear time
        # and constant space
        slow = fast = nums[0]
        while True :
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        while slow != fast :
            slow= nums[slow]
            fast = nums[fast]
        return slow

