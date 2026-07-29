class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashy = defaultdict(list)
        lngSq = 0
        for i in nums:
            if i - 1 not in nums:
                hashy[i].append(i)
                
                chk = i + 1
                lent = 1
                while chk in nums:
                    hashy[i].append(chk)
                    chk += 1
                    lent += 1
                
                if lent > lngSq:
                    lngSq = lent
                    
            
        return lngSq    
        