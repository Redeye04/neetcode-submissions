class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0

        left = 0
        right = len(height) - 1
        prevL = height[left]
        prevR = height[right]

        while left <= right:
            if height[left] < height[right]:
                water += prevL - height[left]
                left += 1
                print(water)
            elif height[right] < height[left]:
                water += prevR - height[right]
                right -= 1
            else:
                right -= 1
            
            if height[left] > prevL:
                prevL = height[left]
            if height[right] > prevR:
                prevR = height[right] 
            
        return water
            