class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # the logic is to use a dictionary to store the occurrences of each number
        # we then sort the numbers by their occurrences in descending order
        # we then return the top k numbers
        # this way, we can get the top k frequent elements in linear time
        # and constant space
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        # sort unique elements by frequency, descending
        sorted_by_freq = sorted(count.keys(), key=lambda num: count[num], reverse=True)

        return sorted_by_freq[:k]
        
        