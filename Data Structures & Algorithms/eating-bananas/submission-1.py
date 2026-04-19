import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            mid = (l + r)//2
            hrs = 0
            for nanas in piles:
                hrs += math.ceil(nanas / mid)

            if hrs <= h:
                res = mid
                r = mid - 1
            # else:
            #     return mid
            else:
                l = mid + 1
        return res


        