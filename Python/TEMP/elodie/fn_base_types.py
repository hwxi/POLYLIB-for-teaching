class FnSint:
    """Functional signed integer - immutable"""
    def __init__(self, value):
        object.__setattr__(self, 'value', value)
    
    def __setattr__(self, name, value):
        raise AttributeError("FnSint is immutale)
        
    def __add__(self, other):
        return FnSint(self.value + other.value)
    
    def __sub__(self, other):
        return FnSint(self.value - other.value)
    
    def __mul__(self, other):
        return FnSint(self.value * other.value)
        
    def __floordiv__(self, other):
        return FnSint(self.value // other.value)
    
    def __mod__(self, other):
        return FnSint(self.value % other.value)
    
    def __neg__(self):
        return FnSint(-self.value)
    
    def __abs__(self):
        return FnSint(abs(self.value))
    
    def __lt__(self, other):
        return self.value < other.value
    
    def __le__(self, other):
        return self.value <= other.value
    
    def __gt__(self, other):
        return self.value > other.value
    
    def __ge__(self, other):
        return self.value >= other.value
        
    def __eq__(self, other):
        if not isinstance(other, FnSint):
            return False
        return self.value == other.value
    
    def __hash__(self):
        return hash(self.value)
    
    def compare_to(self, other):
        """Returns -1, 0, or 1"""
        if self.value < other.value:
            return -1
        elif self.value > other.value: 
            return 1
        return 0
        
    def __str__(self):
        return str(self.value)
    
    def __repr(self):
        return f"FnSint({self.value})"
    
class FnUint:
    """Functional unsigned integer - immutable, non-negative"""
    
    def __init__(self, value):
        if value < 0:
            raise ValueError(f"FnUint must be non-negative, got {value}")
        object.__setattr__(self, 'value', value)
    
    def __setattr__(self, name, value):
        raise AttributeError("FnUint is immutable")
    def __add__(self, other):
        return FnUint(self.value + other.value)
        
    def __sub__(self, other):
        result = self.value - other.value
        if result < 0:
            raise ValueError("FnUint subtraction would be negative")
        return FnUint(result)
    
    def __mul__(self, other):
        return FnUint(self.value * other.value)
        
    def __floordiv__(self, other):
        return FnUint(self.value // other.value)
    
    def __mod__(self, other):
        return FnUint(self.value % other.value)
        
    def __lt__(self, other):
        return self.value < other.value
    
    def __le__(self, other):
        return self.value <= other.value
    
    def __gt__(self, other):
        return self.value > other.value
    
    def __ge__(self, other):
        return self.value >= other.value
        
    def __eq__(self, other):
        if not isinstance(other, FnUint):
            return False
        return self.value == other.value
    
    def __hash__(self):
        return hash(self.value)
    
    def compare_to(self, other):
        if self.value < other.value:
            return -1
        elif self.value > other.value:
            return 1
        return 0
    
    def __str__(self):
        return str(self.value)
        
    def __repr__(self):
        return f"FnUint({self.value})"
    
class FnChar:
    """Functional character - immutable"""
    
    def __init__(self, value):
        if len(value) != 1:
            raise ValueError(f"FnChar must be single character, got '{value}'")
        object.__setattr__(self, 'value', value)
    
    def __setattr__(self, name, value):
        raise AttributeError("FnChar is immutable")
    
    def __lt__(self, other):
        return self.value < self.other
        
    def __le__(self, other):
        return self.value <= self.other
    
    def __gt__(self, other):
        return self.value > self.other
    
    def __ge__(self, other):
        return self.value >= self.other
        
    def __eq__(self, other):
        if not isinstance(other, FnChar):
            return False
        return self.value == other.value 
        
    def __hash__(self):
        return hash(self.value)
    
    def compare_to(self, other):
        if self.value < other.value:
            return -1
        elif self.value > other.value:
            return 1
        return 0
        
    def is_alpha(self):
        return self.value.isalpha()
        
    def is_digit(self):
        return self.value.isdigit()
        
    def is_alphanumeric(self):
        return self.value.isalnum()
    
    def is_whitespace(self):
        return self.value.isspace()
    
    def to_upper(self):
        return FnChar(self.value.upper())
        
    def to_lower(self):
        return FnChar(self.value.lower())
        
    def __str__(self):
        return self.value
    
    def __repr__(self):
        return f"FnChar('{self.value}')"
        
class FnDflt:
    """Functional float - immutable"""
    
    def __init__(self, value):
        object.__setattr__(self, 'value', float(value))
        
    def __setattr__(self, name, value):
        raise AttributeError("FnDflt is immutable")
        
    def __add__(self, other):
        return FnDflt(self.value + other.value)
        
    def __sub__(self, other):
        return FnDflt(self.value - other.value)
        
    def __mul__(self, other):
        return FnDflt(self.value * other.value)
        
    def __truediv__(self, other):
        return FnDflt(self.value / other.value)
        
    def __neg__(self):
        return FnDflt(-self.value)
        
    def __lt__(self, other):
        return self.value < other.value
    
    def __le__(self, other):
        return self.value <= other.value
    
    def __gt__(self, other):
        return self.value > other.value
    
    def __ge__(self, other):
        return self.value >= other.value
        
    def __eq__(self, value):
        if not isinstance(other, FnDflt):
            return False
        return self.value == other.value
    
    def __hash__(self):
        return hash(self.value)
        
    def compare_to(self, value):
        if self.value < other.value:
            return -1
        elif self.value > other.value:
            return 1
        return 0
    
    def sqrt(self):
        return FnDflt(self.value ** 0.5)
        
    def pow(self, exp):
        return str(self.value)
        
    def __repr__(self):
        return f"FnDflt({self.value})"
        
    
    
    
        
    