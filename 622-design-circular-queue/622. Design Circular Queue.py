class Node:
    def __init__(self, nxt, prev, val):
        self.next = nxt
        self.prev = prev
        self.val = val


class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.size = 0
        self.dummyLeft = Node(None, None, -1)
        self.dummyRight = Node(None, None, -1)
        self.dummyLeft.next = self.dummyRight
        self.dummyRight.prev = self.dummyLeft

        #front is left and rear is right
        
        

    def enQueue(self, value: int) -> bool:
        if self.size == self.capacity:
            return False

        newNode = Node(self.dummyRight, None, value)
        if self.dummyRight.prev: #if there are already elts
            oldRear = self.dummyRight.prev
            oldRear.next = newNode
            newNode.prev = oldRear
        elif self.dummyLeft.next == self.dummyRight: #if this is the first elt
            self.dummyLeft.next = newNode
            newNode.prev = self.dummyLeft
        self.dummyRight.prev = newNode
        
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False

        if self.size == 1:
            self.dummyRight.prev = self.dummyLeft
            self.dummyLeft.next = self.dummyRight
            self.size -= 1
            return True
        
        if self.size >= 2:
            newFront = self.dummyLeft.next.next
            self.dummyLeft.next = newFront
            newFront.prev = self.dummyLeft
            self.size -= 1
            return True
        
        
        

    def Front(self) -> int:
        if self.size == 0:
            return -1
        else:
            return self.dummyLeft.next.val
        

    def Rear(self) -> int:
        if self.size == 0:
            return -1
        else:
            return self.dummyRight.prev.val

        

    def isEmpty(self) -> bool:
        return self.size == 0
        

    def isFull(self) -> bool:
        return self.size == self.capacity
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()