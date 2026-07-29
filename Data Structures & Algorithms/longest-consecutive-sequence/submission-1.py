class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        lngSq = 0
        for i in nums:
            if i - 1 not in nums:
                chk = i + 1
                lent = 1
                while chk in nums:
                    chk += 1
                    lent += 1
                
                if lent > lngSq:
                    lngSq = lent
                    
            
        return lngSq    
        