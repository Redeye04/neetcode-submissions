class TimeMap:

    def __init__(self):
        self.hashy = defaultdict(list)
        self.time_prev = -1

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashy[key].append([value, timestamp])
        self.time_prev = timestamp
        return

    def get(self, key: str, timestamp: int) -> str:
        if key in self.hashy:
            curr = ""
            left = 0
            right = len(self.hashy[key]) - 1
            while left <= right:
                mid = (left + right) // 2
                if timestamp >= self.hashy[key][mid][1]:
                    curr = self.hashy[key][mid][0]
                    left = mid + 1
                else:
                    right = mid - 1
            return curr
        return ""