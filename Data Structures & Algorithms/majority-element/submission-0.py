class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = 0
        hashy = {}
        for i in nums:
            if i not in hashy:
                hashy[i] = 1
            else:
                hashy[i] += 1

            if i in hashy and hashy[i] > len(nums)//2:
                return i
        
        return