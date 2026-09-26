class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s = float("infinity")
        final = 0
        for i in prices:
            if i < s:
                s = i
                continue
            final = max(final, i - s)
        
        return final