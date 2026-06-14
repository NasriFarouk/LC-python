class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # the logic is to use a set to store the numbers we have seen
        # if we see a number again, we return True
        # if we reach the end of the array and we have not seen any number again, we return False
        # this way, we can check if the array contains any duplicates in linear time
        # and constant space
        numsSet = set()
        for i in nums :
            if i in numsSet :
                return True
            numsSet.add(i)
        return False
        