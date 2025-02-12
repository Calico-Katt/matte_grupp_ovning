import numpy as np
import math

#v1, v2, n and p needs to be in list-types to work
def projectPointToPlan(p, method = "direction"):
    p_array = np.array(p)
    if method == "direction":
        v1, v2 = interaction(method)
        v1_array, v2_array = np.array(v1), np.array(v2) #Turn list into array gives easier acess to np functions
        #solve ekvation
        a = np.array([[np.dot(v1_array, v1_array), np.dot(v1_array,v2_array)],
                      [np.dot(v2_array, v1_array), np.dot(v2_array, v2_array)]])
        b = np.array([np.dot(p_array, v1_array), np.dot(p_array, v2_array)])
        s, t = np.linalg.solve(a, b)
        p_projection = s*v1_array + t*v2_array

    elif method == "normal":
        n = interaction(method)
        n_array = np.array(n)
        #Sovle ekvation
        proj_n = (np.dot(p_array, n_array) / np.dot(n_array, n_array))*n_array
        p_projection = p_array - proj_n

    else:
        raise ValueError("Method must be 'direction' or 'normal'")
    
    #Depending on which if function is activated, the program will give the projection of the asked ekvation
    return p_projection 


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


if __name__ == "__main__":
    while True:
        method = input("Witch method do you want to use: direction or normal? (direction takes two directed vectors and returns the projection, normal use a normalvector and returns the projection)" + "\n")
        p = list(map(parse_value, input("Enter 'P'(ex. 3, 6, -2): ").strip().split(',')))[:3]
        answer = projectPointToPlan(p, method)
        print(f"The projection: {answer} \n")
        start_stop = input("Klick enter to keep going or write 'quit' to exit program \n").strip().lower()
        if start_stop == "quit":
            print("Exiting program.\n")
            break

