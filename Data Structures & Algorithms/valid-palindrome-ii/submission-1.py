class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        flag = True

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            
            while left < right and s[left] != s[right]:
                p = s[left:right]
                p1 = s[left+1:right+1]
                if p[::-1] == p:
                    return True
                elif p1[::-1] == p1:
                    return True
                return False
        
        return True