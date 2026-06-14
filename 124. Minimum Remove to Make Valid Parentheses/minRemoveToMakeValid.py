class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # the logic is to use a stack to store the indices of the opening parentheses
        # if we encounter a closing parentheses, we check if the stack is empty
        # if it is, we add the index of the closing parentheses to the set of indices to remove
        # if it is not, we pop the top of the stack
        # we then iterate through the stack and add the indices of the opening parentheses to the set of indices to remove
        # we then iterate through the string and add the characters to the answer if the index is not in the set of indices to remove
        # we return the answer as a string
        indexes_to_remove = set()
        stack = []
        for i in range(len(s)):
            if s[i] not in '()':
                continue
            elif s[i] == '(':
                stack.append(i)
            else :
                if not stack :
                    indexes_to_remove.add(i)
                else :
                    stack.pop()
        for i in stack :
            indexes_to_remove.add(i)
        answer = []
        for i in range(len(s)):
            if i not in indexes_to_remove :
                answer.append(s[i])
        return "".join(answer)
        