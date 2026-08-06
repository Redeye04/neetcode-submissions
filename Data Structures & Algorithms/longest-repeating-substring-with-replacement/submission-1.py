class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        maxf = 0
        i = 0
        j = 0
        hashy = {}

        while j < len(s):
            hashy[s[j]] = 1 + hashy.get(s[j], 0)
            if hashy[s[j]] > maxf:
                maxf = hashy[s[j]]
            winSize = (j - i + 1)
            if winSize - maxf <= k:
                print(maxf)
                if winSize > longest:
                    longest = winSize
            else:
                hashy[s[i]] -= 1
                i += 1
            j += 1
        
        return longest