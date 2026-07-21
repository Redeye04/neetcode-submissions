class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashy = defaultdict(list)

        for i in strs:
            
            alps = [0] * 26
            for c in i:
                alps[ord(c) - ord('a')] += 1

            hashy[tuple(alps)].append(i)
        
        return list(hashy.values())