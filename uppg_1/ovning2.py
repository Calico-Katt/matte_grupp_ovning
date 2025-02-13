import numpy as np
import matplotlib.pyplot as plt

#Right know the arguments need to be A = array, v0=tuple, n= int. Easy to change later on.
def ovning(A: np.array, v0: tuple, n: int):
    if n < 0:
        raise ValueError("n needs to be a positive integar")
    if A.shape[0] != 2 or A.shape[1] != 2:
        raise ValueError("A needs to be a 2x2-matrix")
    
    answer_matrix = np.zeros((2, n)) # 2xn-matrix row1 = x-koordinet, row2 = y-koordinet column1 = v0
    v_last = np.array(v0)
    #k vill start att 0 and go to n.
    for k in range(n+1):
        answer_matrix[:, k] = v_last
        v_k = np.matmul(A, v_last)
        v_last = v_k

    #Add matplotlib.scatter and other things here?