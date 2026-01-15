class BinSearch:
    """Binary search for arrays/lists"""
    
    @staticmethod 
    def search(arr, key, cmp):
        """ 
        Binary search in sorted array
        arr: array/list to search
        key: element to find
        cmp: comparison function (returns -1, 0, 1)
        returns: index if found, -1 if not found
        """
        
        lo = 0
        hi = len(arr) - 1
        
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            sgn = cmp(key, arr[mid])
            
            if sgn < 0:
                hi = mid - 1
            elif sgn > 0:
                lo = mid + 1
            else: 
                return mid
            
        return -1 
        
    @staticmethod 
    def search_comparable(arr, key):
        """Binary search for comparable elements"""
        def cmp(a, b):
            if a < b:
                return -1
            elif a > b: 
                return 1
            else: 
                return 0
            
        return BinSearch.search(arr, key, cmp)


