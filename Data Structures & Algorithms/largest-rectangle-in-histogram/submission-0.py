class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #[startindex, val]
        res = 0
        #push to stack while increasing order
        for i, num in enumerate(heights):
            
            newStart = 0
            #if adding in increasing order
            if stack and num > stack[-1][1]:
                stack.append([i, num])

            #if num is <=
            else:
                while stack and num <= stack[-1][1]:

                    res = max(res, (i - stack[-1][0]) * stack[-1][1])
                    newStart = stack[-1][0]
                    stack.pop()
                    #new start index for curr

                stack.append([newStart, num])

        for val in stack:
            res = max(res, (len(heights) - val[0]) * val[1])
        return res

                

