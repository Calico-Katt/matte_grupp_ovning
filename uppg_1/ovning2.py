import numpy as np
import matplotlib.pyplot as plt


def ovning(v0, n, A = None, barnsley = False):
    if n <= 0:
        raise ValueError("n needs to be a positive integar")
    
    answer_matrix = np.zeros((2, n)) # 2xn-matrix row1 = x-koordinet, row2 = y-koordinet column1 = v0
    v_last = np.array(v0)
    #k will start at 0 and go to n.
    for k in range(n):
        if barnsley:
            A, b = Barnsley()
            v_last = np.matmul(A, v_last) + b
        else:
            v_last = np.matmul(A, v_last)
        answer_matrix[:, k] = v_last
        
    #Adds the points and show the graf
    plt.scatter(answer_matrix[0, :], answer_matrix[1, :], color = "blue" if barnsley else "green")
    plt.title("Uppgift b: Barnsleys Ormbunksblad" if barnsley else "Uppgift a")
    plt.show()
    return answer_matrix


def Barnsley():
    A_list = [np.array([[0, 0], [0, 0.16]]),
              np.array([[0.85, 0.04], [-0.04, 0.85]]),
              np.array([[0.2, -0.26], [0.23, 0.22]]),
              np.array([[-0.15, 0.28], [0.26, 0.24]])]
    
    b_list= [np.array([0, 0]),
             np.array([0, 1.6]),
             np.array([0, 1.6]),
             np.array([0, 0.44])]
    
    probabilities = [0.01, 0.85, 0.07, 0.07]

    i = np.random.choice(len(A_list), p = probabilities) #Random selection of A and b depending on the peobabilities
    A_selected = A_list[i]
    b_selected = b_list[i]
    return A_selected, b_selected

def test_ovning_a():
    A = np.random.rand(2, 2) #Changes the answer every test by doing a random 2x2-matrixs
    v0 = (1, 2)
    n = 20
    print(f"Test of 'Uppgift a':\nA = {A}\nv0 = {v0}\nn = {n}\n")
    matrix = ovning(v0, n, A)

def test_ovning_b():
    v0 = (0, 0)
    n = 1000
    print(f"Test of 'Uppgift b':\nv0 = {v0}\nn = {n}\n")
    matrix_barnsley = ovning(v0, n, barnsley = True)

if __name__ == "__main__":
    test_ovning_a()
    test_ovning_b()