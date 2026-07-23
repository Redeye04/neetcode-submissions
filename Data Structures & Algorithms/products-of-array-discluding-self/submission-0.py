class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = nums[:]
        ans[0] = 1
        for i in range(1, len(nums)):
            ans[i] = nums[i - 1] * ans[i - 1]
                
        suffix_pro = 1
        for j in range(len(nums) - 2, -1, -1):
            suffix_pro *= nums[j+1]
            ans[j] *= suffix_pro
        
        return ans
