import numpy as np

def input_matrix(name):
    print(f"\nEnter details for Matrix {name}")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    print(f"Enter the elements of Matrix {name} row-wise:")

    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        while len(row) != cols:
            print(f"Please enter exactly {cols} values.")
            row = list(map(float, input(f"Row {i+1}: ").split()))
        matrix.append(row)

    return np.array(matrix)


def display_matrix(title, matrix):
    print("\n" + "=" * 40)
    print(title)
    print("=" * 40)
    print(matrix)
    print("=" * 40)


while True:
    print("\n===== MATRIX OPERATIONS TOOL =====")
    print("1. Matrix Addition")
    print("2. Matrix Subtraction")
    print("3. Matrix Multiplication")
    print("4. Matrix Transpose")
    print("5. Matrix Determinant")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ")

    if choice == "1":
        A = input_matrix("A")
        B = input_matrix("B")

        if A.shape == B.shape:
            display_matrix("Matrix A", A)
            display_matrix("Matrix B", B)
            display_matrix("Addition Result", A + B)
        else:
            print("Error: Matrices must have the same dimensions.")

    elif choice == "2":
        A = input_matrix("A")
        B = input_matrix("B")

        if A.shape == B.shape:
            display_matrix("Matrix A", A)
            display_matrix("Matrix B", B)
            display_matrix("Subtraction Result", A - B)
        else:
            print("Error: Matrices must have the same dimensions.")

    elif choice == "3":
        A = input_matrix("A")
        B = input_matrix("B")

        if A.shape[1] == B.shape[0]:
            display_matrix("Matrix A", A)
            display_matrix("Matrix B", B)
            display_matrix("Multiplication Result", np.matmul(A, B))
        else:
            print("Error: Number of columns of A must equal number of rows of B.")

    elif choice == "4":
        A = input_matrix("A")
        display_matrix("Original Matrix", A)
        display_matrix("Transpose", A.T)

    elif choice == "5":
        A = input_matrix("A")

        if A.shape[0] == A.shape[1]:
            display_matrix("Matrix", A)
            print("\nDeterminant =", np.linalg.det(A))
        else:
            print("Error: Determinant can only be calculated for square matrices.")

    elif choice == "6":
        print("\nThank you for using Matrix Operations Tool!")
        break

    else:
        print("Invalid choice! Please select a valid option.")