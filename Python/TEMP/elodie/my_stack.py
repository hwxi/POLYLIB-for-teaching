class MyStackEmptyExn(Exception):
    """Exception for empty stack access"""
    pass

class MyStackFullExn(Exception):
    """Exception for full stack push"""
    pass

class MyStack:
    """Abstract stack base class"""
    
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
            raise MyStackEmptyExn("Stack is empty")
        return self.top_raw()
    
    def pop_raw(self):
        raise NotImplementedError
    
    def pop_opt(self):
        return None if self.is_empty() else self.pop_raw()
    
    def pop_exn(self):
        if self.is_empty():
            raise MyStackEmptyExn("Stack is empty")
        return self.pop_raw()
    
    def push_raw(self, item):
        raise NotImplementedError
    
    def push_opt(self, item):
        if self.is_full():
            return False
        self.push_raw(item)
        return True
    
    def push_exn(self, item):
        if not self.push_opt(item):
            raise MyStackFullExn("Stack is full")
        
    def foritm(self, work):
        raise NotImplementedError
        
    def iforitm(self, work):
        i = 0
        def work_with_index(item):
            nonlocal i
            work(i, item)
            i += 1
        self.foritm(work_with_index)
        
        
class MyStackList(MyStack):
    """List-based stack (unlimited)"""
    
    def __init__(self):
        self._items = []
        
    def size(self):
        return len(self._items)
        
    def is_full(self):
        return False 
    
    def top_raw(self):
        return self._items[-1]
    
    def pop_raw(self):
        return self._items.pop()
    
    def push_raw(self, item):
        self._items.append(item)
    
    def foritm(self, work):
        for item in reversed(self._items):
            work(item)
    
    def __str__(self):
        items = ', '.join(str(item) for item in reversed(self._items))
        return f"MyStackList({items})"
    
class MyStackArray(MyStack):
    """Array-based stack (fixed capacity)"""
    
    def __init__(self, capacity):
        if capacity < 1:
            raise ValueError("Capacity must be at least 1")
        self._capacity = Capacity
        self._items = [None] * Capacity
        self._nitm = 0
        
    def size(self):
        return self._nitm
        
    def is_full(self):
        return self._nitm >= self._capacity
        
    def top_raw(self):
        return self._items[self._nitm - 1]
    
    def pop_raw(self):
        self._nitm -= 1
        return self._items[self._nitm]

    def push_raw(self, item):
        self._items[self._nitm] = item
        self._nitm += 1
    
    def foritm(self, work):
        for i in range(self._nitm - 1, -1, -1):
            work(self._items[i])
        
    def __str__(self):
        items = ', '.join(str(self._items[i]) for i in range(self._nitm - 1, -1, -1))
        return f"MyStackArray({items})"
    
    
    
    
    
        
    
    
    
    
