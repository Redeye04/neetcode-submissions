class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lngSeq = 1
        ns = len(s)
        if ns < 2:
            return ns

        i = 0
        j = 1
        seq = set()
        seq.add(s[i])

        while j < len(s):
            if s[j] in seq:
                seq.remove(s[i])
                i += 1
            else:
                seq.add(s[j])
                j += 1
            
            if len(seq) > lngSeq:
                lngSeq = len(seq)

        return lngSeq