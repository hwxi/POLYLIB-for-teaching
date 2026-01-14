class FnA1sz:
    """Functional array - immutable"""
    
    def __init__(self, items):
        if isinstance(items, tuple):
            object.__setattr__(self, '_items', items)
        elif isinstance(items, list):
            object.__setattr__(self, '_items', tuple(items))
        elif isinstance(items, FnA1sz):
            object.__setattr__(self, '_items', items._items)
        else:
            object.__setattr__(self, '_items', tuple(items))
        
    def __setattr__(self, name, value):
        raise AttributeError("FnA1sz is immutable")
        
    def get_at(self, i):
        """get element at index"""
        return self._items[i]
    
    def length(self):
        """Get length"""
        return len(self._items)
    
    def foritm(self, work):
        """Iterate over elements"""
        for item in self._items:
            work(item)
        
    def iforitm(self, work):
        """iterate with index"""
        for i, item in enumerate(self._items):
            work(i, item)
    
    def forall(self, pred):
        """Check if all satisfy predicate"""
        for item in self._items:
            if not pred(item):
                return False
        return True
    
    def map(self, f):
        """Map function over array"""
        return FnA1sz(tuple(f(item) for item in self._items))
        
    def imap(self, f):
        """Map indexed function"""
        return FnA1sz(tuple(f(i, item) for i, item in enumerate(self._items)))
        
    def filter(self, pred):
        """Filter by predicate"""
        return FnA1sz(tuple(item for item in self._items if pred(item)))
    
    def fold_left(self, init, f):
        """Fold from left"""
        result = init
        for item in self._items:
            result = f(result, item)
        return result
        
    def reverse(self):
        """Reverse array"""
        return FnA1sz(tuple(reversed(self._items)))

    def __getitem__(self, i):
        return self._items[i]
    
    def __len__(self):
        return len(self._items)
    
    def __iter__(self):
        return iter(self._items)
    
    def __str__(self):
        items = ', '.join(str(item) for item in self._items)
        return f"FnA1sz({items})"
        
    def __repr__(self):
        return self.__str__()
    
def fn_array_int1_make(n):
    """Create an array [0, 1, ..., n-1]"""
    return FnA1sz(tuple(range(n)))
    
    
    