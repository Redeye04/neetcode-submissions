class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashy = defaultdict(list)
        for i in strs:
            word = "".join(sorted(i))
            hashy[word].append(i)

        return list(hashy.values())