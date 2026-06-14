class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # the logic is to use two pointers, prev and after
        # we iterate through the array and multiply the previous element by the current element
        # we then iterate through the array and multiply the next element by the current element
        # we return the result
        # this way, we can get the product of the array except self in linear time
        # and constant space
        n = len(nums)
        result = [1]*n
        prev = after = 1
        for i in range(1,n):
            result[i]= prev * nums[i-1]
            prev = result[i]
        for i in range(n-2,-1,-1):
            result[i]= result[i] * nums[i+1] * after
            after = nums[i+1] * after
        return result
