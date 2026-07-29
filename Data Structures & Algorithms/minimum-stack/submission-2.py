class MinStack:

    def __init__(self):
        self.stack = []
        self.s2 = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.s2 != [] and self.s2[-1] >= val:
            self.s2.append(val)
        elif self.s2 == []:
            self.s2.append(val)
        
        return None

    def pop(self) -> None:
        if self.stack == []:
            return None
        
        if self.s2 != [] and self.stack[-1] == self.s2[-1]:
            self.s2.pop()

        self.stack.pop()
        return None

    def top(self) -> int:
        if self.stack == []:
            return -1
        
        return self.stack[-1]


    def getMin(self) -> int:
        if self.stack == [] or self.s2 == []:
            return -1
        return self.s2[-1]
