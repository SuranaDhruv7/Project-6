import numpy as np
print("Welcome to the NumPy Analyzer!")
print("------------------------------")
print("------------------------------\n")
class DataAnalytics:
    def all_functionalities(self, element_wise_addition, element_wise_subtraction, element_wise_multiplication, element_wise_division, dot_product_matrix_multipliction):
        self.element_wise_addition = element_wise_addition
        self.element_wise_subtraction = element_wise_subtraction
        self.element_wise_multiplication = element_wise_multiplication
        self.element_wise_division = element_wise_division
        self.dot_product_matrix_multipliction = dot_product_matrix_multipliction

    def display(self):
        print (f"Addition: {self.element_wise_addition}, Substaction: {self.element_wise_subtraction}, Multiplicatuion: {self.element_wise_multiplication}, Division: {self.element_wise_division}, Dot Multiplication: {self.dot_product_matrix_multipliction}")
elems = []
is_on = True
while is_on:
    print("Choose an option: ")
    print("1. Create a Numpy Array")
    print("2. Perform Mathematical Operations")
    print("3. Combine or Split Arrays")
    print("4. Search, Sort, or Filter Arrays")
    print("5. Compute Aggregates and Statistics")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        type = int(input("Select the type of array to create:\n1. 1D Array\n2. 2D Array\n3. 3D Array\nEnter your choice: "))
        if type == 1:
            new_rows = int(input("Enter the number of rows: "))
            new_columns = int(input("Enter the number of columns: "))
            elems = (int(input("Enter elems: ")))
            for i in range(elems):
                i.append(input(f"Enter elements for the array: "))
        elif type == 2:
            new_rows = int(input("Enter the number of rows: "))
            new_columns = int(input("Enter the number of columns: "))
            elems = (int(input("Enter elems: ")))
            for i in range(elems):
                i.append(input(f"Enter elements for the array: "))
                pass
        elif type == 3:
            new_rows = int(input("Enter the number of rows: "))
            new_columns = int(input("Enter the number of columns: "))
            elems = (int(input("Enter elems: ")))
            for i in range(elems):
                i.append(input(f"Enter elements for the array: "))
                pass
        else:
            print("INVALID TYPE!")
        operation1 = int(input("Choose an operation:\n1. Indexing\n2. Slicing\n3. Go Back\nEnter your choice: "))
        if operation1 == 1:
            row_range = input("Enter the row range (start::end): ")
            column_range = input("Enter the column range (start::end): ")
            pass
        elif operation1 == 2:
            row_range = input("Enter the row range (start::end): ")
            column_range = input("Enter the column range (start::end): ")
            pass
        elif operation1 == 3:
            row_range = input("Enter the row range (start::end): ")
            column_range = input("Enter the column range (start::end): ")
            pass
        else:
            print("INVALID OPERATION!")
    elif choice == 2:
        mathe_operation = int(input("Choose a mathematical operation:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\nEnter your choice: "))
        if mathe_operation == 1:
            element_wise_addition =
            print("element_wise_addition")
        elif mathe_operation == 2:
             element_wise_subtraction =
             print("element_wise_subtraction")
        
        elif mathe_operation == 3:
            element_wise_multiplication =
            print("element_wise_multiplication")
        
        elif mathe_operation == 4:
            element_wise_division =
            print("element_wise_division")
        else:
            print("INVALID MATHEMATICAL OPERATION!")
    elif choice == 3:
        option = int(input("Choose an option:\n1. Combine Arrays\n2. Split Arrays\nEnter your choice: "))
        if type == 1:
            pass
        elif type == 1:
            pass
    elif choice == 4:
        option = int(input("Choose an option:\n1. Search a value\n2. Sort the array\n3. Filter values\nEnter your choice: "))
        if option == 1:
            pass
        elif option == 1:
            pass
        elif option == 1:
            pass
        else:
            print("INVALID OPTION!")
    elif choice == 5:
        operation = int(input("Choose an aggregate/statistical operation:\n1. Sum\n2. Mean\n3. Median\n4. Standard Deviation\n5. Variance\nEnter your choice: "))
        if operation == 1:
            pass
        elif operation == 1:
            pass
        elif operation == 1:
            pass
        elif operation == 1:
            pass
        elif operation == 1:
            pass
        else:
            print("INVALID OPERATION!")
    elif choice == 6:
        print("\nThankyou for using the NumPY Analyzer! GOODBYE!\n")
        is_on = False

    else:
        print("\nINVALID CHOICE! PLEASE ENTER THE CORRECT CHOICE!\n")
        is_on = False