class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 0
        least = prices[left]
        greatest = 0
        while right < len(prices):
            if prices[right] < least:
                left = right
                least = prices[left]
            greatest = max(greatest, prices[right] - prices[left])
            right += 1

        return greatest
