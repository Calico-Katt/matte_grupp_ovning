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

def kl():
    pass

def uppgiftA():
    A = Matrix([[1, 2, 1, -1, 2],
                [3, 4, 5, 2, 0],
                [2, 2, 1, 0, 2]])
    print("\nUppgift A\n")
    rref(A)


if __name__ == "__main__":
    uppgiftA()





