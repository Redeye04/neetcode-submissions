class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        hashy = {}
        n = len(nums)
        for i in nums:
            if i not in hashy:
                hashy[i] = 1
            else:
                hashy[i] += 1
            
            if hashy[i] > n // 3 and i not in ans:
                ans.append(i)
            
        return ans