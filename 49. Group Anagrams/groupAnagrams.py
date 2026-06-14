class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # the logic is to use a dictionary to store the occurrences of each character in the string
        # we then iterate through the string and add the occurrences of each character to the array
        # we then iterate through the array and check if the occurrences of each character is 0
        # if it is not, we return False
        # if we reach the end of the array and all the occurrences are 0, we return True
        # this way, we can check if the two strings are anagrams in linear time
        # and constant space
        anargramDict = {}
        for word in strs :
            occurances = [0]*26
            for i in word :
                occurances[ord(i)-ord('a')] += 1
            if tuple(occurances) in anargramDict :
                anargramDict[tuple(occurances)].append(word)
            else :
                anargramDict[tuple(occurances)] = [word]
        result = []
        for arr in anargramDict.values() :
            result.append(arr)
        return result
        