class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def determinHrs(rate, piles):
            hrs = 0
            for i in piles:
                if i <= rate:
                    hrs += 1
                else:
                    if i % rate == 0:
                        hrs += i // rate
                    else:
                        hrs += (i // rate) + 1
            return hrs
        
        rang = range(1, max(piles) + 1)
        left = 0
        right = len(rang) - 1

        while left <= right:
            mid = (left + right) // 2
            hrs = determinHrs(rang[mid], piles)
            if hrs <= h:
                right = mid - 1
            elif hrs > h:
                left = mid + 1
        
        return rang[left]
        