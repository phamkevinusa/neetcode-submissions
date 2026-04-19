class Solution:
    def trap(self, height: List[int]) -> int:
        #water height determined by lowest of highest points on either side - height at i  
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)

        #handle left height
        m = 0
        for l in range(1, len(height)-1):
            m = max(m, height[l-1])
            maxLeft[l] = m

        m = 0
        for r in range(len(height)-2,0,-1):
            m = max(m, height[r + 1])
            maxRight[r] = m

        res = 0
        for i in range(len(height)):
           # print(min(maxLeft[i], maxRight[i]) - height[i])
            if min(maxLeft[i], maxRight[i]) - height[i] > 0:
                res += min(maxLeft[i], maxRight[i]) - height[i]

        return res