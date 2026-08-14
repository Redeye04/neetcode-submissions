class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] + 1 == 10:
            carry = 1
            digits[-1] += 1
            for i in range(len(digits) - 1, -1, -1):
                if digits[i] // 10 == 1:
                    print(digits)
                    if i == 0:
                        digits[i] = 1
                        digits.append(0)
                        break
                    digits[i] = 0
                    digits[i-1] += 1
                    
                else:
                    break
        else:
            digits[-1] += 1
            
        return digits