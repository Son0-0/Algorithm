# https://leetcode.com/problems/design-hashmap
class MyHashMap:

    def __init__(self):
        self.s = dict()

    def put(self, key: int, value: int) -> None:
        self.s[key] = value

    def get(self, key: int) -> int:
        if key in self.s:
            return self.s[key]
        return -1

    def remove(self, key: int) -> None:
        if key in self.s:
            del(self.s[key])


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
