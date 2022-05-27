# https://leetcode.com/problems/design-circular-queue
from collections import deque

class MyCircularQueue:

    def __init__(self, k: int):
        self.q = deque()
        self.length = k
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.size < self.length:
            self.q.append(value)
            self.size += 1
            return True
        
    def deQueue(self) -> bool:
        if self.q:
            self.q.popleft()
            self.size -= 1
            return True

    def Front(self) -> int:
        if self.size:
            return self.q[0]
        return -1
        
    def Rear(self) -> int:
        if self.size:
            return self.q[-1]
        return -1

    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        return False
        
    def isFull(self) -> bool:
        if self.size == self.length:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()