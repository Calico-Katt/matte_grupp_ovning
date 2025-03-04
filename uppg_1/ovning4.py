import numpy as np
from scipy import linalg as LA
from sympy import Matrix
import time

A = Matrix([[1, 2, 1, -1, 2],
              [2, 4, 5, 2, 0],
              [2, 2, 1, 0, 2]])


def uppA():
    # Skapar en matris på formen [A|0]
    totA = A.row_join(Matrix([[0], [0], [0]]))

    # Löser systemet med Gausseliminering (rref)
    rref_matrix, pivot_columns = totA.rref()

    print("Reducerad matris:")
    print(rref_matrix)

uppA()