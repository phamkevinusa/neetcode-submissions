class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque() # stores index, not value
        l = r = 0

        while r < len(nums):

            #while in increasing order
            while q and nums[q[-1]] < nums[r]:
                q.pop() #remove the smallest values(no need to look anymmore)
            q.append(r)

            if l > q[0]: # remove indexes no longer needed
                q.popleft()

            if (r+1) >= k: # in iterations after window reaches size, begin providing output and incrementing left
                output.append(nums[q[0]])
                l += 1

            r += 1

        return output