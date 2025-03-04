import numpy as np
from scipy import linalg as LA
from sympy import Matrix
import time

def rref(A):
    rref_matrix, pivot_columns = A.rref()
    print(f"Radreducerad matris:\n{rref_matrix}\nPivotkolonner: {pivot_columns}")
    free_variables_columns = [i for i in range(A.shape[1]) if i not in pivot_columns]
    solutions = rref_matrix.nullspace()
    "Need to add the free variables with t, s, v... so the solution makes more seens, and check so the positiv and negativ works"
    if solutions:
        print()
        for idx, sol in enumerate(solutions):
            print(f"x_{idx} = {sol}")

def uppgiftA():
    A = Matrix([[1, 2, 1, -1, 2],
                [3, 4, 5, 2, 0],
                [2, 2, 1, 0, 2]])
    rref(A)


if __name__ == "__main__":
    uppgiftA()





