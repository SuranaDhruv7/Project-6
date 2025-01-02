import numpy as np
print("Welcome to the NumPy Analyzer!")
print("---------------------------------")
print("---------------------------------")
class DataAnalytics:
    def create_1D_array(self):
        n = int(input("Enter the number of elements: "))
        l = [int(input("Enter elem: ")) for i in range(n)]
        array = np.array(l)
        return array
    
    def create_2D_array(self):
        rows = int(input("Enter the number of rows: "))
        cols = int(input("Enter the number of columns: "))
        print(f"Enter {rows*cols} elements for the array: ")
        l = [int(input("Enter elem: ")) for i in range(rows*cols)]
        array = np.array(l).reshape(rows, cols)
        return array
    
    def create_3D_array(self):
        rows = int(input("Enter the number of rows: "))
        cols = int(input("Enter the number of columns: "))
        print(f"Enter {rows*cols} elements for the array: ")
        l = [int(input("Enter elem: ")) for i in range(rows*cols)]
        array = np.array(l).reshape(2, rows, cols)
        a = []
        a.append(array)
        return np.array(a)
    
    def search_value(self, array):
        elem = int(input("Enter elem to be searched: "))
        is_elem_founded = False
        for i in array:
            for j in i:
                if j == elem:
                    is_elem_founded = True
        if is_elem_founded:
            print("Elem founded!")
        else:
            print("Elem not fouded!")
obj = DataAnalytics()
is_on = True
while is_on:
    print("Choose an option: ")
    print("1. Create a Numpy Array")
    print("2. Perform Mathematical Operations")
    print("3. Combine or Split Arrays")
    print("4. Search, Sort, or Filter Arrays")
    print("5. Compute Aggregates and Statistic")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Select the type of array to create: ")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")
        operation = int(input("Enter your choice: "))
        if operation == 1:
            array = obj.create_1D_array()
            print("Array created successfully: ")
            print(array)
            print("Choose an operation: ")
            print("1. Indexing")
            print("2. Slicing")
            print("3. Go Back")
            opt = int(input("Enter your choice: "))
            if opt == 1:
                index = int(input("Enter any index: "))
                print(f"Your value is {array[index]}")
            elif opt == 2:
                start_val = int(input("Enter start index val: "))
                end_val = int(input("Enter end index val: "))
                print(f"Your range/slice is {array[start_val:end_val]}")
            elif opt == 3:
                break
            else:
                print("INVALID OPTION! PLEASE ENTER THE CORRECT OPTION!")
        
        elif operation == 2:
            array = obj.create_2D_array()
            print("Array created successfully: ")
            print(array)
            print("Choose an operation: ")
            print("1. Indexing")
            print("2. Slicing")
            print("3. Go Back")
            opt = int(input("Enter your choice: "))
            if opt == 1:
                row_index = int(input("Enter row index: "))
                col_index = int(input("Enter col index: "))
                print(f"Your value is {array[row_index][col_index]}")
            elif opt == 2:
                start_val = int(input("Enter start index val: "))
                end_val = int(input("Enter end index val: "))
                print(f"Your range/slice (row-wise) is {array[start_val:end_val]}")
            elif opt == 3:
                break
            else:
                print("INVALID OPTION! PLEASE ENTER THE CORRECT OPTION!")
            
        elif operation == 3:
            array = obj.create_3D_array()
            print("Array created successfully: ")
            print(array)
            print("Choose an operation: ")
            print("1. Indexing")
            print("2. Slicing")
            print("3. Go Back")
            opt = int(input("Enter your choice: "))
            if opt == 1:
                block_index = int(input("Enter block index (0 and 1): "))
                row_index = int(input("Enter row index: "))
                col_index = int(input("Enter col index: "))
                print(f"Your value is {array[block_index][row_index][col_index]}")
            elif opt == 2:
                block_index = int(input("Enter block index (0 and 1): "))
                start_val = int(input("Enter start index val: "))
                end_val = int(input("Enter end index val: "))
                print(f"Your range/slice (row-wise) is {array[block_index, start_val:end_val, :]}")
            elif opt == 3:
                break
            else:
                print("INVALID OPTION! PLEASE ENTER THE CORRECT OPTION!")
        else:
            print("INVALID TYPE!")
    
    elif choice == 2:
        array1 = obj.create_1D_array()
        array2 = obj.create_2D_array()
        print("Choose a mathematical operation: ")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        option = int(input("Enter vour choice: "))
        if option == 1:
            print(array1 + array2)
        elif option == 2:
            print(array1 - array2)
        elif option == 3:
            print(array1*array2)
        elif option == 4:
            print(array1 / array2)
        else:
            print("INVALID CHOICE!")
    elif choice == 3:
        array1 = obj.create_2D_array()
        print(array1)

        array2 = obj.create_2D_array()
        print(array2)
        
        print("Choose an option: ")
        print("1. Combine")
        print("2. Split")
        option = int(input("Enter your choice: "))
        if option == 1:
            print("How to combine arrays?")
            print("1. Horizontal stack")
            print("2. Vertical stack")
            stacks = int(input("Enter the type of combine array: "))
            if stacks == 1:
                combined_array = np.hstack(array1)
                print(f"Original array: {array1, array2}")
                print(f"Combined array: {combined_array}")
            elif stacks == 2:
                combined_array = np.vstack(array1)
                print(f"Original array: {array1, array2}")
                print(f"Combined array: {combined_array}")
            else:
                print("INVALID CHOICE!")
        elif option == 2:
            print("How to split arrays?")
            print("1. Horizontal split")
            print("2. Vertical split")
            stacks = int(input("Enter the type of split array: "))
            if stacks == 1:
                splitted_array = np.hsplit(array1, 2)
                print(f"Original array: {array1}")
                print(f"Splitted array: {splitted_array}")
            elif stacks == 2:
                array1_reshaped = array1.reshape(2, 2)
                splitted_array = np.vsplit(array1_reshaped, 2)
                print(f"Original array: {array1_reshaped}")
                print(f"Splitted array: {splitted_array}")
            else:
                print("INVALID CHOICE!")
        else:
            print("INVALID CHOICE!")
    elif choice == 4:
        array = obj.create_2D_array()
        print(array)
        print("Choose an option: ")
        print("1. Search a value")
        print("2. Sort the array")
        print("3. Filter values")
        option = int(input("Enter your choice: "))
        if option == 1:
            obj.search_value(array)
        elif option == 2:
            print("How to sort values?")
            print("1. Ascending")
            print("2. Descending")
            option = int(input("Enter the type of sort: "))
            if option == 1:
                sorted_array = np.sort(array)
                print(f"Original array: {array}")
                print(f"Sorted array (Ascending): {sorted_array}")
            elif option == 2:
                sorted_array = np.sort(array)[::-1]
                print(f"Original array: {array}")
                print(f"Sorted array (Descending): {sorted_array}")
        elif option == 3:
            val = int(input("Enter any value: "))
            filtered_array = array[array < val]
            print(f"Filtered array (All elements which are lesser than {val}): {filtered_array}")
        else:
            print("INVALID CHOICE!")
    elif choice == 5:
        array = obj.create_2D_array()
        print(array)

        print("Choose an aggregate/statistical operation: ")
        print("1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Variance")
        option = int(input("Enter your choice: "))
        if option == 1:
            print(f"Sum: {np.sum(array)}")
        elif option == 2:
            print(f"Mean: {np.mean(array)}")
        elif option == 3:
            print(f"Median: {np.median(array)}")
        elif option == 4:
            print(f"Standard Deviation: {np.std(array)}")
        elif option == 5:
            print(f"Variance: {np.var(array)}")
        else:
            print("INVALID CHOICE!")
    elif choice == 6:
        print("\nThankyou for using Numpy Analyzer! GOODBYE!\n")
        is_on = False
    else:
        print("\nINVALID OPTION! PLEASE ENTER THE CORRECT CHOICE!\n")
        is_on = False