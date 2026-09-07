class MyHashSet:

    def __init__(self):
        self.hashy = {}

    def add(self, key: int) -> None:
        if key not in self.hashy:
            self.hashy[key] = 0
        return

    def remove(self, key: int) -> None:
        if key in self.hashy:
            self.hashy.pop(key)
        return

    def contains(self, key: int) -> bool:
        if key in self.hashy:
            return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)