class FnTree:
    """Functional binary tree - immutable"""
    
    def __init__(self, item = None, lchild = None, rchild = None):
        object.__setattr__(self. '_item', item)
        object.__setattr__(self, '_lchild', lchild)
        object.__setattr__(self, '_rchild', rchild)

    def __setattr__(self, name, value):
        raise AttributeError("FnTree is immutable")
        
    def nilq(self):
        """Check if empty"""
        return self._item is None
        
    def consq(self):
        """Check if non-empty"""
        return self._item is not None
    
    def item(self):
        """Get root item"""
        if self._item is None:
            raise ValueError("item() on empty tree")
        return self._item
        
    def lchild(self):
        """Get left child"""
        if self._lchild is None:
            return FnTree()
        return self._lchild
    
    def rchild(self):
        """Get right child"""
        if self._rchild is None:
            return FnTree()
        return self._rchild
    
    def size(self):
        """Count nodes"""
        if self.nilq():
            return 0
        return 1 + self.lchild().size() + self.rchild().size()
    
    def height(self):
        """Get height"""
        if self.nilq():
            return 0
        return 1 + max(self.lchild().height(), self.rchild().height())
    
    def inorder(self, work):
        """Inorder traversal: left, root, right"""
        if self.nilq():
            return
        self.lchild().inorder(work)
        work(self.item())
        self.rchild().inorder(work)
        
    def preorder(self, work):
        """Preorder traversal: root, left, right"""
        
        if self.nilq():
            return 
        work(self.item())
        self.lchild().preorder(work)
        self.rchild().preorder(work)
    
    def postorder(self, work):
        """Postorder traversal: left, right, root"""
        if self.nilq():
            return
        self.lchild().postorderorder(work)
        self.rchild().postorder(work)
        work(self.item())
        
    def __str__(self):
        if self.nilq():
            return "FnTree()"
        items = []
        self.inorder(lambda x : items.append(str(x)))
        return f"FnTree({', '.join(items)})"

def fn_tree_nil():
    """Create empty tree"""
    return FnTree()
    
def fn_tree_leaf(item):
    """Create leaf node"""
    return FnTree(item, FnTree(), FnTree())

def fn_tree_node(item, left, right):
    """Create tree node"""
    return FnTree(item, left, right)
    









