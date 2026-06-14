class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # the logic is to use a dictionary to store the numbers we have seen and their indices
        # if we see a number again, we check if the difference between the current index and the index of the number is less than or equal to k
        # if it is, we return True
        # if we reach the end of the array and we have not seen any number again, we return False
        # this way, we can check if the array contains any duplicates in linear time
        # and constant space
        numsDict = {}
        for i in range(len(nums)):
            if nums[i] in numsDict :
                if abs(i-numsDict[nums[i]]) <= k :
                    return True
            numsDict[nums[i]] = i
        return False  
        