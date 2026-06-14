class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # the logic is to use an array to store the occurrences of each character in the string
        # we then iterate through the string and add the occurrences of each character to the array
        # we then iterate through the array and check if the occurrences of each character is 0
        # if it is not, we return False
        # if we reach the end of the array and all the occurrences are 0, we return True
        # this way, we can check if the two strings are anagrams in linear time
        # and constant space
        if len(s) != len(t):
            return False
        occurances = [0]*26
        for i in range(len(s)):
            occurances[ord(s[i]) - ord('a')] += 1
            occurances[ord(t[i]) - ord('a')] -= 1
        for i in occurances :
            if i != 0 :
                return False
        return True