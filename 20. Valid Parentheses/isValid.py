class Solution:
    def isValid(self, s: str) -> bool:
        # the logic is to use a stack to store the opening parentheses
        # if we encounter a closing parentheses, we check if the top of the stack is the corresponding opening parentheses
        # if it is, we pop the top of the stack
        # if it is not, we return False
        # if we encounter a closing parentheses and the stack is empty, we return False
        # if we reach the end of the string and the stack is not empty, we return False
        # if we reach the end of the string and the stack is empty, we return True
        stack = []
        for i in s :
            if i in ['(', '[','{']:
                stack.append(i)
            else :
                if len(stack) == 0:
                    return False
                last_element = stack.pop()
                if i == ')' and last_element != '(':
                    return False
                if i == '}' and last_element != '{':
                    return False
                if i == ']' and last_element != '[':
                    return False
        return len(stack) == 0 
                
        