import numpy as np
from scipy import linalg as LA
from sympy import Matrix, symbols
import time

def rref(A):
    rref_matrix, pivot_columns = A.rref()
    print(f"Radreducerad matris:\n{rref_matrix}\nPivotkolonner: {pivot_columns}")
    total_columns = A.shape[1]
    free_variables_columns = [i for i in range(total_columns) if i not in pivot_columns]
    solutions = rref_matrix.nullspace()
    free_symbols = symbols("t s v w z")[:len(free_variables_columns)]
    free_variables_symbol = {f"x{var+1}": sym for var, sym in zip(free_variables_columns, free_symbols)}
    x_solutions = Matrix.zeros(total_columns, 1)
    if solutions:
        print("Fria variabler:")
        for var, sym in free_variables_symbol.items():
            print(f"{var} = {sym}")
        print(f"Där {', '.join(map(str, free_symbols))} ∈ ℝ.\n")
        print("Lösning till Ax = 0")
        for free_variables, symbol, solution in zip(free_variables_columns, free_symbols, solutions):
                x_solutions += symbol * solution
        print(f"x = {x_solutions}\n")

def rref_time(A, y):
    A_tot = A.row_join(y)
    start_time = time.time()
    rref_matrix, pivot_column = A_tot.rref()
    left_matrix = rref_matrix[:, :-1]
    right_matrix = rref_matrix[:, -1]
    if left_matrix[:, :rref_matrix.shape[0]].is_Identity:
        print(f"Unik lösning:\nx = {right_matrix}")
        x_matrix = right_matrix
    else:
        print("Ingen eller oändligt med lösningar hittade")
    elapsed_time = time.time() - start_time
    print(f"\nBeräkningstid: {elapsed_time}\n")
    return x_matrix

def verify_solutions(A, x, y):
    print("Checkar så A*x - y ≈ 0")
    if x:
        remaining = (A * x) - y
        if all(abs(rem) < 1e-7 for rem in remaining):
            print("Lösningen verifierades vara korrekt")
            return
        print("Lösningen verifierades vara inkorrekt")
    else: 
        print("Ingen lösning att verifiera.")

def invers(A, y):
    start_time = time.time()
    A_invers = LA.inv(A)
    x_solution = np.matmul(A_invers, y)
    elapsed_time = time.time() - start_time
    print(f"Lösning till Ax = y\nA = {A}\ny = {y}\nTar gånger inversen av A på båda sidorna vilket get x = A^-1 * y\nx = {x_solution}\nBeräkningstid: {elapsed_time}")
    return x_solution

def uppgiftA():
    A = Matrix([[1, 2, 1, -1, 2],
                [3, 4, 5, 2, 0],
                [2, 2, 1, 0, 2]])
    print("\nUppgift A\n")
    rref(A)

def uppgiftB():
    print("Uppgift B")
    A = Matrix(np.random.rand(100, 100))
    y = Matrix(np.random.rand(100, 1))
    print("Användning av np.random.rand()")
    x_rand = rref_time(A, y)
    verify_solutions(A, x_rand, y)
    A_int= Matrix(np.random.randint(low = -10, high = 10, size = (100, 100)))
    y_int = Matrix(np.random.randint(low = -10, high = 10, size = (100, 1)))
    print("\nAnvändning av np.random.randint")
    x_randint = rref_time(A_int, y_int)
    verify_solutions(A_int, x_randint, y_int)
    

def uppgiftC():
    print("\nUppgift C")
    A = np.array(np.random.rand(100, 100))
    y = np.array(np.random.rand(100, 1))
    print("Användning av np.random.rand()")
    x = invers(A, y)
    verify_solutions(Matrix(A), Matrix(x), Matrix(y))
    A_int= np.array(np.random.randint(low = -10, high = 10, size = (100, 100)))
    y_int = np.array(np.random.randint(low = -10, high = 10, size = (100, 1)))
    print("\nAnvändning av np.random.randint")
    x_int = invers(A_int, y_int)
    verify_solutions(Matrix(A_int), Matrix(x_int), Matrix(y_int))


if __name__ == "__main__":
    uppgiftA()
    uppgiftB()
    uppgiftC()