import numpy as np
import matplotlib.pyplot as plt

A = np.array([[0.7, 0.1, 0.3],
              [0.1, 0.6, 0.2],
              [0.2, 0.3, 0.5]])

def uppgiftA():
    print(f"From the information given in the instructions\n A = {A}\n (row 1= Centralen, row2 = Landvetter, row 3 = uthyrda)\n")
    print("v1 = A* v0\nv2 = A^2 * v0\nvn = A^n * v0\n(v2 = A* v1 -> v2 = A*A*v0 = A^2 * v0)\n")

def uppgiftB():
    v0 = np.array([[(1/3)],
                   [(1/3)],
                   [(1/3)]])
    v0_1 = np.array([[1],
                    [0],
                    [0]])
    v0_2 = np.array([[0],
                     [1],
                     [0]])
    v0_3 = np.array([[0],
                     [0],
                     [1]])
    timerList = [1, 10, 100, 1000, 10000, 100000]
    print(f"Uppgift B\n v0 = {v0}\nweeks being checked = {timerList}\n")
    carDistributionGraph(v0, timerList)
    print(f"v0 = {v0_1}\nweeks being checked = {timerList}\n")
    carDistributionGraph(v0_1, timerList)
    print(f"v0 = {v0_2}\nweeks being checked = {timerList}\n")
    carDistributionGraph(v0_2, timerList)
    print(f"v0 = {v0_3}\nweeks being checked = {timerList}\n")
    carDistributionGraph(v0_3, timerList)


def carDistributionGraph(v0, timeList):
    "row1 = cn, row2 = ln, row3 = un"
    carDistributionMatrix = np.zeros((3, len(timeList)))
    for k in range(0, len(timeList)):
        vn = np.matmul(np.linalg.matrix_power(A, timeList[k]), v0)
        carDistributionMatrix[:, k] = vn.flatten()
    
    plt.plot(timeList, carDistributionMatrix[0, :], label = "Centralen", color = "cyan")
    plt.scatter(timeList, carDistributionMatrix[0, :], color = "blue")
    plt.plot(timeList, carDistributionMatrix[1, :], label = "Landvetter", color = "palegreen")
    plt.scatter(timeList, carDistributionMatrix[1, :], color = "green")
    plt.plot(timeList, carDistributionMatrix[2, :], label = "rented out", color = "pink")
    plt.scatter(timeList, carDistributionMatrix[2, :], color = "red")
    plt.title("Car distribution as a function of time")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    uppgiftA()
    uppgiftB()
