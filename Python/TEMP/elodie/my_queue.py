class MyQueueEmptyExn(Exception):
    """Exception for empty queue access"""
    pass

class MyQueueFullExn(Exception):
    """Exception for full queue enqueue"""
    pass

class MyQueue: 
    """Abstract queue base class"""
    
    def size(self):
        raise NotImplementedError
    
    def is_full(self):
        raise NotImplementedError
        
    def is_empty(self):
        return self.size() <= 0
    
    def top_raw(self):
        raise NotImplementedError
        
    def top_opt(self):
        return None if self.is_empty() else self.top_raw()
    
    def top_exn(self):
        if self.is_empty():
            raise MyQueueEmptyExn("Queue is empty")
        return self.top_raw()
        
    def deque_raw(self):
        raise NotImplementedError
    
    def deque_opt(self):
        return None if self.is_empty() else self.deque_raw()
        
    def deque_exn(self):
        if self.is_empty():
            raise MyQueueEmptyExn("Queue is empty")
        return self.deque_raw()
        
    def enque_raw(self, item):
        raise NotImplementedError
        
    def enque_opt(self, item):
        if self.is_full():
            return False
        self.enque_raw(item)
        return True
        
    def enque_exn(self, item):
        if not self.enque_opt(item):
            raise MyQueueFullExn("Queue is full")
            
    def foritm(self, work):
        raise NotImplementedError
        
    def iforitm(self, work):
        i = 0
        def work_with_index(item):
            nonlocal i
            work(i, item)
            i += 1
        self.foritm(work_with_index)

class MyQueueList(MyQueue):
    """List-based queue (unlimited)"""
    
    def __init__(self):
        self._items = []
        
    def size(self):
        return len(self._items)
    
    def is_full(self):
        return False
    
    def top_raw(self):
        return self._items[0]
    
    def deque_raw(self):
        return self._items.pop(0)
    
    def enque_raw(self, item):
        self._items.append(item)
    
    def foritm(self, work):
        for item in self._items:
            work(item)
    
    def __str__(self):
        items = ', '.join(str(item) for item in self._items)
        return f"MyQueueList({items})"
        
class MyQueueArray(MyQueue):
    """Array-based circular queue (fixed capacity)"""
    
    def __init__(self, capacity):
        if capacity < 2: 
            raise ValueError("Capacity must be at least 2")
        self._capacity = capacity
        self._items = [None] * capacity
        self._frst = 0
        self._last = 0
        self._nitm = 0
        
    def size(self):
        return self._nitm
        
    def is_full(self):
        return self._nitm >= self._capacity
        
    def top_raw(self):
        return self._items[self._frst]
        
    def deque_raw(self):
        item = self._items[self._frst]
        self._frst = (self._frst + 1) % self._capacity
        self._nitm -= 1
        return item
    
    def enque_raw(self, item):
        self._items[self._last] = item
        self._last = (self._last + 1) % self._capacity
        self._nitm += 1
    
    def foritm(self, work):
        for i in range(self._nitm):
            work(self._items[(self._frst + i) % self._capacity])
    
    def __str__(self):
        items = ', '.join(str(self._items[(self._frst + i)% self._capacity]) for i in range(self._nitm))
        return f"MyQueueArray({items})"
    
        
            
    
    
    
    
    