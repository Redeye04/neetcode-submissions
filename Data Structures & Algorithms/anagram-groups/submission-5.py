class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashy = defaultdict(list)
        for i in strs:
            alp = [0] * 26
            for j in i:
                ind = ord(j) - ord('a')
                alp[ind] += 1
            
            hashy[tuple(alp)].append(i)

        return list(hashy.values())