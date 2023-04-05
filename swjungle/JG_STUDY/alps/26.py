# https://leetcode.com/problems/design-circular-deque
from collections import deque

class MyCircularDeque:

    def __init__(self, k: int):
        self.q = deque()
        self.length = k
        self.size = 0
        
        
    def insertFront(self, value: int) -> bool:
        if self.size < self.length:
            self.q.appendleft(value)
            self.size += 1
            return True
        return False
        

    def insertLast(self, value: int) -> bool:
        if self.size < self.length:
            self.q.append(value)
            self.size += 1
            return True
        return False
        

    def deleteFront(self) -> bool:
        if self.size != 0:
            self.q.popleft()
            self.size -= 1
            return True
        return False
        

    def deleteLast(self) -> bool:
        if self.size != 0:
            self.q.pop()
            self.size -= 1
            return True
        return False
        

    def getFront(self) -> int:
        if self.q:
            return self.q[0]
        return -1
        

    def getRear(self) -> int:
        if self.q:
            return self.q[-1]
        return -1
        

    def isEmpty(self) -> bool:
        if not self.q:
            return True
        return False
        

    def isFull(self) -> bool:
        if self.size == self.length:
            return True
        return False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()