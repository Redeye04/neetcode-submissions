class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            leng = len(i)
            res += str(leng)+"#"+i
        print(res)
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        str1 = ""
        i = 0
        prev = 0
        while i < len(s):
            leng = ""
            
            if s[i] == "#":
                chek = i - 1
                while s[chek] in ['1','2','3','4','5','6','7','8','9','0'] and chek > prev-1:
                    leng += s[chek]
                    chek -= 1
                leng = leng[::-1]
                res.append(s[i+1:i+int(leng)+1])
                i += int(leng)+1
                prev = i
            else:
                str1 += s[i]
                i += 1
                        
        return res