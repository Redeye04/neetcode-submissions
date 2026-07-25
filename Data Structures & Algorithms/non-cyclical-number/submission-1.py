class Solution:
    def isHappy(self, n: int) -> bool:
        hashy = {}

        def sumer(n):
            sum1 = 0
            for i in str(n):
                sum1 += int(i) ** 2
            
            return sum1

        while n != 1:
            if n in hashy:
                return False
            hashy[n] = 0
            n = sumer(n)
        
        return True