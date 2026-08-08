class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        pairs = [[p, s] for p, s in zip(position, speed)]

        # Sorted because no cars are passing each other
        for p, s in sorted(pairs)[::-1]:
            stack.append((target - p) / s)

            # If the car on left reaches the target first or in same time it passes the car in front so we remove the car to make it as one fleet.
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)