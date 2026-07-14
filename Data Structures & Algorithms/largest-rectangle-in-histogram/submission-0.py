
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                #Pop stack 
                index, height = stack.pop()
                # check max rectangle
                maxArea = max(maxArea, height * (i - index))
                # extent current height backwards
                start = index
            stack.append((start, h))
        # maxArea for remaining items which could not be popped 
        # but which can be extended till the end
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea
