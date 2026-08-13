class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashy = defaultdict(list)
        for i in range(len(strs)):
            chars = [0] * 26
            for j in strs[i]:
                chars[(ord(j) - ord('a')) % 26] += 1
            hashy[tuple(chars)].append(strs[i])

        return list(hashy.values())