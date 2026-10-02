class Node:
    def __init__(self, prev, val, nxt):
        self.prev = prev
        self.val = val
        self.nxt = nxt

class LRUCacheLinkedList:
    # a linked list tracks LRU key nodes O(1) pop, insert, delete
    # a hashmap points to those linked list nodes for O(1) retrival
    # pop from left (Left is LRU)
    def __init__(self, head):
        self.dummyFront = Node(None, None, None)
        self.dummyTail = Node(None, None, None)
        self.head = Node(self.dummyFront, head, self.dummyTail)
        self.dummyFront.nxt = self.head
        self.dummyTail.prev = self.head
        self.nodes = {}
        self.nodes[head] = self.head
    def remove(self, key):
        node = self.nodes[key]
        prev = node.prev
        nxt = node.nxt
        
        prev.nxt = nxt
        nxt.prev = prev
        self.nodes.pop(key)
    def getLRU(self):
        return self.dummyFront.nxt.val

    def insert(self, key):
        new = Node(None, key, None)
        self.nodes[key] = new
        prev = self.dummyTail.prev
        
        prev.nxt = new
        self.dummyTail.prev = new

        new.nxt = self.dummyTail
        new.prev = prev
        self.nodes[key] = new
    

class LFUCache:
    def __init__(self, capacity: int):
        self.cache = defaultdict(int) # hashmap solves get; key : int
        
        # have a linked list for each frequency count (retrived w/ hashmap for O(1))
        self.freqCountToLRU = {} # int : LRUCacheLinkedList

        # return the front of the linked list for a tracked minValue frequency count (updated in O(1) as we operate, checking if a linked list is empty as we remove). Make minValue a stack, where you keep on adding elements to the front if they are smaller (pop if that linked list is empty)
        self.minFreqValue = -1 #updated as you go in O(1) avg
        self.capacity = capacity
        self.curHold = 0
        self.values = defaultdict(int)

    def useKey(self, key):
        old_freq = self.cache[key]
        if self.cache[key] in self.freqCountToLRU:
            self.freqCountToLRU[self.cache[key]].remove(key)
            
        self.cache[key] += 1
        if (self.cache[key]) in self.freqCountToLRU:
            self.freqCountToLRU[self.cache[key]].insert(key)
        else:
            self.freqCountToLRU[self.cache[key]] = LRUCacheLinkedList(key)
        if self.minFreqValue == old_freq and len(self.freqCountToLRU[self.minFreqValue].nodes) == 0:
            self.minFreqValue = old_freq + 1
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.useKey(key)
            return self.values[key]
        return -1
        
    def eject(self):
        key = self.freqCountToLRU[self.minFreqValue].getLRU()
        self.curHold -= 1
        self.freqCountToLRU[self.minFreqValue].remove(key)
        self.cache.pop(key)

        
            


    def put(self, key: int, value: int) -> None:

        
        if key not in self.cache:
            if self.curHold == self.capacity:
                self.eject()
            self.cache[key] = 0
            self.minFreqValue = 1
            self.curHold += 1

        self.values[key] = value
        self.useKey(key)





        

        



        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)