class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        n1 = len(s1)
        lis1 = [0] * 26
        lis2 = [0] * 26
        for k in range(n1):
            lis1[(ord(s1[k]) - ord('a'))] += 1
            lis2[(ord(s2[k]) - ord('a'))] += 1
        
        matches = 0
        for i in range(26):
            if lis1[i] == lis2[i]:
                matches += 1
        print(matches)

        l = 0
        for j in range(n1, len(s2)):
            if matches == 26:
                return True
            
            ind = ord(s2[j]) - ord('a')
            lis2[ind] += 1
            if lis2[ind] == lis1[ind]:
                matches += 1
            elif lis1[ind] + 1 == lis2[ind]:
                matches -= 1
            
            ind = ord(s2[l]) - ord('a')
            lis2[ind] -= 1
            if lis2[ind] == lis1[ind]:
                matches += 1
            elif lis1[ind] - 1 == lis2[ind]:
                matches -= 1
            l += 1

        return matches == 26