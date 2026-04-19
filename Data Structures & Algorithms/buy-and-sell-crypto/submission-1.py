class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        l, r = 0, 1
        while r < len(prices):
            res = max(res, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r
                r = l + 1
            elif prices[r] >= prices[l]:
                r = r + 1

        return res