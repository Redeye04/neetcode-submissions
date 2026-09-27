class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if '0' in [num1, num2]:
            return '0'

        num1, num2 = num1[::-1], num2[::-1]

        digits = [0] * (len(num1) + len(num2))
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])
                digits[i1 + i2] += digit
                digits[i1 + i2 + 1] += digits[i1 + i2] // 10
                digits[i1 + i2] = digits[i1 + i2] % 10
        
        digits = digits[::-1]
        beg = 0
        while beg < len(digits) and digits[beg] == 0:                
            beg += 1

        return "".join(map(str, digits[beg:]))