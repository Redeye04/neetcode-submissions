class Solution:
    def isPalindrome(self, s: str) -> bool:
        original = ""
        for i in s:
            if i.isalnum():
                original += i.lower()
        rev = original[::-1]
        print(rev)
        if rev == original:
            return True
        return False