if __name__ == "__main__":
    print("=" * 70)
    print("PYTHON FUNCTIONAL LIBRARY - Complete Implementation")
    print("No external library imports")
    print("=" * 70)
    
    # Base types
    print("\n1. Base Types (fn_base_types.py)")
    print("-" * 70)
    a = FnSint(10)
    b = FnSint(5)
    print(f"FnSint: {a} + {b} = {a + b}")
    print(f"FnSint: {a} * {b} = {a * b}")
    
    x = FnUint(15)
    y = FnUint(3)
    print(f"FnUint: {x} // {y} = {x // y}")
    
    c = FnChar('A')
    print(f"FnChar: {c}.to_lower() = {c.to_lower()}")
    
    d = FnDflt(9.0)
    print(f"FnDflt: sqrt({d}) = {d.sqrt()}")
    
    # Reference
    print("\n2. Mutable Reference (my_refer.py)")
    print("-" * 70)
    ref = MyRefer(42)
    print(f"ref = {ref.get_raw()}")
    ref.set_raw(100)
    print(f"After set: {ref.get_raw()}")
    
    # List
    print("\n3. Functional List (fn_list.py)")
    print("-" * 70)
    lst = fn_list_int1_make(10)
    print(f"List: {lst}")
    print(f"Length: {lst.length()}")
    
    squared = lst.map(lambda x: x * x)
    print(f"Squared: {squared}")
    
    sum_val = lst.fold_left(0, lambda acc, x: acc + x)
    print(f"Sum: {sum_val}")
    
    # Array
    print("\n4. Functional Array (fn_array.py)")
    print("-" * 70)
    arr = fn_array_int1_make(10)
    print(f"Array: {arr}")
    print(f"arr[5] = {arr[5]}")
    
    doubled = arr.map(lambda x: x * 2)
    print(f"Doubled: {doubled}")
    
    # Tuples
    print("\n5. Functional Tuples (fn_tuple.py)")
    print("-" * 70)
    pair = FnTupl2("Alice", 25)
    print(f"Pair: {pair}")
    name, age = pair
    print(f"Unpacked: name={name}, age={age}")
    
    triple = FnTupl3("CS", 392, "A")
    print(f"Triple: {triple}")
    
    print("\n" + "=" * 70)
    print("All components working! Only built-in Python used.")
    print("=" * 70)
    
    
    
    