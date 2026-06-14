class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # the logic is to use a stack to store the indices of the opening parentheses
        # if we encounter a closing parentheses, we check if the stack is empty
        # if it is, we add the index of the closing parentheses to the stack
        # if it is not, we pop the top of the stack
        # we then calculate the length of the valid parentheses by subtracting the index of the opening parentheses from the index of the closing parentheses
        # we update the maximum length if the current length is greater than the maximum length
        # we return the maximum length
        stack = [-1]
        maxAns = 0
        for i in range(len(s)):
            if s[i] == '(' :
                stack.append(i)
            else :
                stack.pop()
                if not stack :
                    stack.append(i)
                else :
                    maxAns = max(maxAns,i-stack[-1])
        return maxAns