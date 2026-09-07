class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = strs[0]

        for i in strs:
            pref = ''
            for j in range(len(longest)):
                if j >= len(i) or longest[j] != i[j]:
                    break
                if longest[j] == i[j]:
                    pref += i[j]
            longest = pref

        return longest