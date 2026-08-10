class Solution:
    def findMin(self, nums: List[int]) -> int:
        cmp1 = nums[0]

        left = 0
        right = len(nums) - 1
        if len(nums) == 2:
            if nums[left] < nums[right]:
                return nums[left]
            else:
                return nums[right]

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] > cmp1:
                left = mid + 1
            elif nums[mid] <= cmp1:
                cmp1 = nums[mid]
                right = mid - 1
        
        return cmp1