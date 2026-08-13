class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        ans = []
        deque = collections.deque()
        l = 0
        r = 0
        while r < len(nums):
            while deque and nums[deque[-1]] < nums[r]:
                deque.pop()
            deque.append(r)

            if deque[0] < l:
                deque.popleft()
            
            if r+1 >= k:
                ans.append(nums[deque[0]])
                l += 1
            r += 1
 
        return ans