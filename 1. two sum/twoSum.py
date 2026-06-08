class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # the logic is to save the seen values with their indexes in a dictionary
        # then, for each number, we check if the remaining value is in the dictionary
        # if it is, we return the indexes of the two numbers
        # if it is not, we add the number and its index to the dictionary
        # this way, we can check if the remaining value is in the dictionary in linear time respectively
        seen = {}
        for i, num in enumerate(nums):
            remaining = target - num
            if remaining in seen:
                return [seen[remaining], i]
            seen[num] = i