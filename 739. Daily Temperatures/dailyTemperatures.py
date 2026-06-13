class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # the logic is to use a stack to store the indices of the temperatures
        # if the current temperature is greater than the temperature at the index at the top of the stack, we pop the index from the stack
        # and we set the result at the index to the current index - the index at the top of the stack
        # we then push the current index to the stack
        # we return the result
        n = len(temperatures)
        stack = []
        result = [0] * n
        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i] :
                last_idx = stack.pop()
                result[last_idx] = i - last_idx
            stack.append(i)
        return result 
        