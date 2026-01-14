class FnList:
    """Immutable single-linked list"""
    
    def __init__(self, head = None, tail = None):
        object.__setattr__(self, '_head', head)
        object.__setattr__(self, '_tail', tail)
    
    def __setattr__(self, name, value):
        raise AttributeError("FnList is immutable")
    def nilq(self):
        """Check if empty"""
        return self._head is None
        
    def consq(self):
        """Check if non-empty"""
        return self._head is not None
        
    def hd(self):
        """Get head"""
        if self._head is None:
            raise ValueError("hd() on empty list")
        return self._head
        
    def tl(self):
        """Get tail"""
        if self._tail is None:
            raise ValueError("tl() on empty list")
        return self._tail
    
    def length(self):
        """Get length"""
        count = 0
        current = self
        while current.consq():
            count += 1
            current = current.tl()
        return count
    
    def reverse(self):
        """Reverse list"""
        result = FnList()
        current = self
        while current.consq():
            result = FnList(current.hd(), result)
            current = current.tl()
        return result
        
    def append(self, other):
        """Append another list"""
        if self.nilq():
            return other
        return FnList(self.hd(), self.tl().append(other))
        
    def foritm(self, work):
        """Iterate over elements"""
        current = self
        while current.consq():
            work(current.hd())
            current = current.tl()
        
    def iforitm(self, work):
        """Iterate with index"""
        i = 0
        current = self
        while current.consq():
            work(i, current.hd())
            i += 1
            current = current.tl()
            
    def forall(self, pred):
        """Check if all satisfy predicate"""
        current = self
        while current.consq():
            if not pred(current.hd()):
                return False
            current = current.tl()
        return True
    
    def map(self, f):
        """Map function over list"""
        if self.nilq():
            return FnList()
        return FnList(f(self.hd()), self.tl().map(f))
    
    def filter(self, pred):
        """Filter by predicate"""
        result = FnList()
        current = self
        while current.consq():
            if pred(current.hd()):
                result = FnList(current.hd(), result)
            current = current.tl()
        return result.reverse()

    def fold_left(self, init, f):
        """Fold from left"""
        result = init
        current = self
        while current.consq():
            result = f(result, current.hd())
            current = current.tl()
        return result
    
    def __str__(self):
        if self.nilq():
            return "FnList()"
        items = []
        self.foritm(lambda x : items.append(str(x)))
        return f"FnList({', '.join(items)})"
        
    def __repr__(self):
        return self.__str__()
    
    def __iter__(self):
        current = self
        while current.consq():
            yield current.hd()
            current = current.tl()

def fn_list_nil():
    """Create empty list"""
    return FnList()
    
def fn_list_cons(head, tail):
    """Cons head onto tail"""
    return FnList(head, tail)

def fn_list_from_items(*items):
    """Create list from items"""
    result = FnList()
    for item in reversed(items):
        result = FnList(item, result)
    return result
    
def fn_list_int1_make(n):
    """Create list [0, 1, ..., n-1]"""
    result = FnList()
    for i in range(n-1, -1, -1):
        result = FnList(i, result)
    return result
    
    