class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # the logic is to use a stack to store the indices of the heights
        # if the current height is less than the height at the index at the top of the stack, we pop the index from the stack
        # and we calculate the area with the height at the index at the top of the stack and the current index
        # we then push the current index to the stack
        # we return the maximum area
        # we append a 0 to the heights array to handle the last element
        # we iterate through the heights array
        # we use a while loop to pop the indices from the stack until the current height is greater than the height at the index at the top of the stack
        # we calculate the area with the height at the index at the top of the stack and the current index
        # we update the maximum area
        # we push the current index to the stack
        # we return the maximum area
        n= len(heights)
        stack = []
        max_area = 0
        heights.append(0)
        for i in range(n+1):
            while stack and heights[stack[-1]] > heights[i]:
                height = heights[stack.pop()]
                index = stack[-1] + 1 if stack else 0
                width = i - index 
                max_area = max(max_area,height*width)
            stack.append(i)
        return max_area
        