class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashy = {}

        for i in s:
            if i not in hashy:
                hashy[i] = 1
            else:
                hashy[i] += 1
        for j in t:
            if j not in hashy:
                return False
            
            hashy[j] -= 1

            if hashy[j] < 0:
                return False

        return True
        
        