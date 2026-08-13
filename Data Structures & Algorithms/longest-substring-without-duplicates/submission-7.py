class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        lngSeq = 1
        
        hashy = {}
        hashy[s[0]] = 1
        l = 0
        for r in range(1, len(s)):
            while s[r] in hashy:
                hashy.pop(s[l], None)
                l += 1
            
            hashy[s[r]] = 1
            curr = (r - l) + 1
            if curr > lngSeq:
                lngSeq = curr
            
        return lngSeq