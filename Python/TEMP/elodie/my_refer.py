class MyReferNullExn(Exception):
    """Exception for null reference access"""
    pass

class MyRefer:
    """Mutable reference wrapper"""
    def __init__(self, value = None):
        self._value = value
    
    def is_null(self):
        return self._value is None
        
    def get_raw(self):
        return self._value
        
    def get_opt(self):
        return self._value
        
    def get_exn(self):
        if self.is_null():
            raise MyReferNullExn("Reference is null")
        return self._value
        
    def set_raw(self, value):
        self._value = value
        
    def takeout_raw(self):
        value = self._value
        self._value = None
        return value
        
    def discard_raw(self):
        self._value = None
        
    def exch_raw(self, new_value):
        old_value = self._value
        self._value = new_value
        return old_value
        
    def __repr__(self):
        return f"MyRefer({self._value})"
        
        