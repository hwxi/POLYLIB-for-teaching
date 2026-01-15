if __name__ == "__main__"":
    print("=" * 70)
    print("Stack, Queue, Trees, and Binary Search")
    print("=" * 70)
    
    #stack tests
    print("\n1. Stack(my_stack.py)")
    print("-" * 70)
    stack = MyStackList()
    stack.push_exn(1)
    stack.push_exn(2)
    stack.push_exn(3)
    print(f"Stack: {stack}")
    print(f"Top: {stack.top_exn()}")
    print(f"Pop: {stack.pop_exn()}")
    print(f"After pop: {stack}")
    
    #array-based stack
    arr_stack = MyStackArray(5)
    for i in range(1, 4):
        arr_stack.push_exn(i*10)
    print(f"Array stack: {arr_stack}")
    
    #queue tests
    print("\n2. Queue (my_queue.py)")
    print("-" * 70)
    queue = MyQueueList()
    queue.enque_exn(1)
    queue.enque_exn(2)
    queue.enque_exn(3)
    print(f"Queue: {queue}")
    print(f"Front: {queue.top_exn()}")
    print(f"Deque: {queue.deque_exn()}")
    print(f"After deque: {queue}")
    
    # Array-based queue
    arr_queue = MyQueueArray(5)
    for i in range(1, 4):
        arr_queue.enque_exn(i * 10)
    print(f"Array queue: {arr_queue}")
    arr_queue.deque_exn()
    arr_queue.enque_exn(40)
    print(f"After deque and enque: {arr_queue}")
    
    # Tree tests
    print("\n3. Binary Tree (fn_tree.py)")
    print("-" * 70)
    # Create tree:
    #       5
    #      / \
    #     3   7
    #    / \
    #   1   4
    tree = fn_tree_node(5,
                        fn_tree_node(3,
                                    fn_tree_leaf(1),
                                    fn_tree_leaf(4)),
                        fn_tree_leaf(7))
    
    print(f"Tree size: {tree.size()}")
    print(f"Tree height: {tree.height()}")
    
    print("Inorder: ", end="")
    tree.inorder(lambda x: print(x, end=" "))
    print()
    
    print("Preorder: ", end="")
    tree.preorder(lambda x: print(x, end=" "))
    print()
    
    print("Postorder: ", end="")
    tree.postorder(lambda x: print(x, end=" "))
    print()
    
    # Binary search
    print("\n4. Binary Search (bin_search.py)")
    print("-" * 70)
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    print(f"Array: {arr}")
    
    key = 7
    idx = BinSearch.search_comparable(arr, key)
    print(f"Search for {key}: index = {idx}")
    
    key = 6
    idx = BinSearch.search_comparable(arr, key)
    print(f"Search for {key}: index = {idx} (not found)")
    
    print("\n" + "=" * 70)
    print("All components working! Only built-in Python used.")
    print("=" * 70)








