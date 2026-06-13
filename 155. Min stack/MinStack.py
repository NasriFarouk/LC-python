class MinStack:
    # the logic is to use a stack to store the values
    # and a minStack to store the minimum values
    # when we push a value, we push it to the stack
    # and we push it to the minStack if it is the minimum value
    # when we pop a value, we pop it from the stack
    # and we pop it from the minStack if it is the minimum value
    # when we get the minimum value, we return the top of the minStack
    # when we get the top value, we return the top of the stack

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.minStack or value <= self.minStack[-1]:
            self.minStack.append(value)
        

    def pop(self) -> None:
        if len(self.stack) == 0 :
            raise IndexError('pop from empty stack')
        value = self.stack.pop()
        if self.minStack and value == self.minStack[-1] :
            self.minStack.pop()
        

    def top(self) -> int:
        if len(self.stack) == 0 :
            raise IndexError('top from empty stack')
        return self.stack[-1]
        

    def getMin(self) -> int:
        if self.minStack :
            return self.minStack[-1]
        return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()