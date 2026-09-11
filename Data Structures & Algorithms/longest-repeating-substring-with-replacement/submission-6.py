class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        maxf = 0
        maxi = 0
        hashy = {}

        l = 0
        for r in range(len(s)):
            hashy[s[r]] = hashy.get(s[r], 0) + 1
            maxf = max(hashy[s[r]], maxf)
            if hashy[s[r]] == maxf:
                maxi = s[r]

            window = (r - l) + 1
            while (window - maxf) > k:
                if s[l] != maxi:
                    hashy[s[l]] -= 1
                    l += 1
                    window = (r - l) + 1
                    break
                hashy[s[l]] -= 1
                l += 1
                window = (r - l) + 1

            longest = max(longest, window)

        return longest
