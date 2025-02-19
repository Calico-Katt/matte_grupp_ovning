import numpy as np
import math

#v1, v2, n and p needs to be in list-types to work
def projectPointToPlan(p, u= None, v = None, n = None, method = "direction"):
    p_array = np.array(p)
    if method == "direction":
        #u, v = interaction(method)
        u_array, v_array = np.array(u), np.array(v) #Turn list into array gives easier acess to np functions

        #solve ekvation
        a = np.array([[np.dot(u_array, u_array), np.dot(u_array,v_array)],
                      [np.dot(v_array, u_array), np.dot(v_array, v_array)]])
        b = np.array([np.dot(p_array, u_array), np.dot(p_array, v_array)])
        s, t = np.linalg.solve(a, b)
        p_projection = s*u_array + t*v_array

    elif method == "normal":
        #n = interaction(method)
        n_array = np.array(n)
        #Sovle ekvation
        proj_n = (np.dot(p_array, n_array) / np.dot(n_array, n_array))*n_array
        p_projection = p_array - proj_n

    else:
        raise ValueError("Method must be 'direction' or 'normal'")
    
    #Depending on which if function is activated, the program will give the projection of the asked ekvation
    return p_projection 


def test_ovning_b():
    P = [math.pi, math.e, 1]
    u = [1, 1, 0]
    v = [0, -1, 0]
    v_negativ = [0, 1, 0]
    print(f"Uppgift b\nP = {P}\nu = {u}\nv = {v}\nprojection 1 = {projectPointToPlan(P, u = u, v = v, method='direction')}")
    print(f"P = {P}\nu = {u}\n-v = {v_negativ}\nprojection 2 = {projectPointToPlan(P, u = u, v = v_negativ, method='direction')}\nProjection 1 = Projection 2 \nIf v turns into -v the only thing that changes is the direction of the vector, the surface area are the same. In the ekvation the diffrent direction on the vector will only result in a new s or t value, this is because of the unchanged p and value of kordinets for the vectors (|v| = |-v|).\n")

def test_ovning_c():
    P = [math.pi, math.e, 1]
    n = [1, 1, 1]
    m = [3, 3, 3]
    print(f"Uppgift c\nP = {P}\nn = {n}\n projection 1 = {projectPointToPlan(P, n = n, method = "normal")}")
    print(f"P = {P}\nm = {m}\nprojection 2 = {projectPointToPlan(P, n = m, method = "normal")}\nIn this case n and m is pointing in the same direction and m = 3*n, witch makes the vectors parallel to each other and the reason the answer is the same.\n")

if __name__ == "__main__":
    test_ovning_b()
    test_ovning_c()


"Below here is extra, a interaction part that can be added if wanted"
def interaction(method):
    if method == "direction":
        vector1 = list(map(parse_value, input("Enter the first vector (ex. 2, 3, -1): ").strip().split(',')))[:3]
        vector2 = list(map(parse_value, input("Enter the secend vector (ex. 3, 6, -2): ").strip().split(',')))[:3]
        return vector1, vector2
    elif method == "normal":
        nVector = list(map(parse_value, input("Enter the normal vector (ex. 3, 6, -2): ").strip().split(',')))[:3]
        return nVector

def parse_value(value):
    valid_numbers = {
        "π" : math.pi,
        "e" : math.e}
    value = value.strip()
    if value in valid_numbers:
        return valid_numbers[value]
    return float(value)


def main_interation():
    while True:
        method = input("Witch method do you want to use: direction or normal? (direction takes two directed vectors and returns the projection, normal use a normalvector and returns the projection)" + "\n")
        p = list(map(parse_value, input("Enter 'P'(ex. 3, 6, -2): ").strip().split(',')))[:3]
        answer = projectPointToPlan(p, method)
        print(f"The projection: {answer} \n")
        start_stop = input("Klick enter to keep going or write 'quit' to exit program \n").strip().lower()
        if start_stop == "quit":
            print("Exiting program.\n")
            break


'''
Motivation why this is correct:
The program has been tested with different variables/arguments and all come back with correct and reasonable results.
'''