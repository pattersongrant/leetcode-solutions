class Node:
    def __init__(self, key = None, next = None, prev = None, val = None):
        self.key = key
        self.next = next
        self.prev = prev
        self.val = val

class LRUCache:
    '''
    linked list stores keys and values

    cache points to linked list node

    head.next is LRU
    '''

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.tail = Node(None, None)
        self.head = Node(None, self.tail, None)
        self.tail.prev = self.head
        
    def insert(self, key, value): #assumes it is already in the cache
        if key in self.cache:
            node = self.cache[key]
            old_prev = self.tail.prev
            old_prev.next = node
            self.tail.prev = node
            node.prev = old_prev
            node.next = self.tail
        else:
            self.cache[key] = Node(key, None, None, value)
            self.insert(key, value)

    def remove(self, key):
        node = self.cache[key]
        old_prev = node.prev
        old_next = node.next
        if old_prev:
            old_prev.next = old_next
        if old_next:
            old_next.prev = old_prev
        node.next, node.prev = None, None
        self.cache.pop(key)

        #remove from wherever (just take away pointers and remove from cache)

    def get(self, key: int) -> int:
        if key in self.cache:
            old_val = self.cache[key].val
            self.remove(key)
            self.insert(key, old_val)
            return self.cache[key].val
        
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(key)
            self.insert(key, value)
            self.cache[key].val = value
        else:
            self.cache[key] = Node(key, None, None, value)
            self.insert(key, value)
        
        if len(self.cache) > self.cap:
            print(self.head.next.key)
            self.remove(self.head.next.key)




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)