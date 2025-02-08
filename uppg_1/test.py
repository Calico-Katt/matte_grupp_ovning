import numpy as np

def projectPointToPlan(p, method = "direction", v1=None, v2=None, n=None):
    p_array = np.array(p)
    if method == "direction":
        #Need to input a interaction function that asks for the two vectors and check so the list have 3 positions. Value error might need to be moved to interaction.
        if v1 is None or v2 is None:
            raise ValueError("Two direction vectors needs too be given for the method 'direction'")
        v1_array, v2_array = np.array(v1), np.array(v2) #Think it might be easier to make the vectors in to arrays instead of list because of the functions in np.
        #solve ekvation not sure this is rights need more time to check
        a = np.array([[np.dot(v1_array, v1_array), np.dot(v1_array,v2_array)],
                      [np.dot(v2_array, v1_array), np.dot(v2_array, v2_array)]])
        b = np.array([np.dot(p_array, v1_array), np.dot(p_array, v2_array)])
        s, t = np.linalg.solve(a, b)
        p_projection = s*v1_array + t*v2_array

    elif method == "normal":
        #Add a input of the normal vector, with the help of an interactive function
        if n is None:
            raise ValueError("A normal vector needs to be given for the method normal to work")
        n_array = np.array(n)
        #Sovle scalar projection (i think I'm really not sure but is making the ekvation in the book in to code)
        u = np.dot(p_array, n_array) / np.dot(n_array, n_array)
        p_projection = p_array - u * n_array
    else:
        raise ValueError("Method must be 'direction' or 'normal'")
    #Depending on which if function is activated, the program will give the projection of the asked ekvation
    return p_projection 

