class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # the logic is to use a stack to store the numbers
        # if we encounter a number, we push it to the stack
        # if we encounter an operator, we pop the top two numbers from the stack
        # we perform the operation on the two numbers
        # we push the result back to the stack
        # we return the top of the stack
        stack = []
        for i in tokens :
            if i not in '+-*/':
                stack.append(int(i))
            else :
                v1= stack.pop()
                v2= stack.pop()
                if i == '+' :
                    stack.append(v1+v2)
                elif i == '-' :
                    stack.append(v2-v1)
                elif i == '*' :
                    stack.append(v1*v2)
                elif i == '/':
                    stack.append(int(v2/v1))
        return stack[0]