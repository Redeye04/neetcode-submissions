class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        window, counts = {}, {}

        for i in t:
            counts[i] = counts.get(i, 0) + 1
            
        need = len(counts)
        have = 0
        res = [-1, -1]
        resLen = float("infinity")
        print(need)

        l = 0
        for r in range(0, len(s)):
            ch = s[r]
            window[ch] = window.get(ch, 0) + 1

            if ch in counts and window[ch] == counts[ch]:
                have += 1
                
            while have == need:
                if (r - l) + 1 < resLen:
                    res = [l, r]
                    resLen = (r - l) + 1
                window[s[l]] -= 1
                if s[l] in counts and counts[s[l]] > window[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""


