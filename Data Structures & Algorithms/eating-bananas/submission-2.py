class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left = 1
        right = max(piles)
        ans = right

        while left <= right:
            mid = (right + left) // 2

            total = 0
            for i in piles:
                total += math.ceil(i / mid)
            
            if total <= h:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return ans