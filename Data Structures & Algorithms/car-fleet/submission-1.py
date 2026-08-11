class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs = [[p,s] for p, s in zip(position, speed)]
        pairs.sort()
        
        for pos, s in pairs[::-1]:
            time = (target - pos) / s
            if len(stack) > 0:
                if time <= stack[-1]:
                    continue
            stack.append(time)
        
        return len(stack)
