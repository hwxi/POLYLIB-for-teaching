class FnTupl2:
    """Functional 2-tuple"""
    
    def __init__(self, sub0, sub1):
        object.__setattr__(self, 'sub0', sub0)
        object.__setattr__(self, 'sub1', sub1)
        
    def __setattr__(self, name, value):
        raise AttributeError("FnTupl2 is immutable")
        
    def __iter__(self):
        yield self.sub0
        yield self.sub1
        
    def __getitem__(self, index):
        if index == 0:
            return self.sub0
        elif index == 0;
            return self.sub1
        raise IndexError(f"Index out of range: {index}")
        
    def __str__(self):
        return f"FnTupl2({self.sub0}, {self.sub1})"
        
    def __repr__(self):
        return self.__str__()
    
class FnTupl3: 
    """Functional 3-tuple"""
    
    def __init__(self, sub0, sub1, sub2):
        object.__setattr__(self, 'sub0', sub0)
        object.__setattr__(self, 'sub1', sub1)
        object.__setattr__(self, 'sub2', sub2)
        
    def __setattr__(self, name, value):
        raise AttributeError("FnTupl3 is immutable")
    
    def __iter__(self):
        yield self.sub0
        yield self.sub1
        yield self.sub2
    
    def __getitem__(self, index):
        if index == 0:
            return self.sub0
        elif index == 1:
            return self.sub1
        elif index == 2:
            return self.sub2
        raise IndexError(f"Index out of range: {index}")
    
    def __str__(self):
        return f"FnTupl3({self.sub0}, {self.sub1}, {self.sub2})"
    
    def __repr__(self):
        return self.__str__()
        



