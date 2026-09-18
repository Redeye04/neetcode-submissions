class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashy = defaultdict(list)
        for s in strs:
            counts = [0] * 26
            for alp in s:
                counts[ord(alp) - ord('a')] += 1
            hashy[tuple(counts)].append(s)
        return list(hashy.values())