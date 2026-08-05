class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        ans = [0] * n

        for i in range(n):
            while stack and stack[-1][0] < temperatures[i]:
                elm = stack.pop()
                ans[elm[1]] = i - elm[1]
            stack.append([temperatures[i], i])

        return ans
        