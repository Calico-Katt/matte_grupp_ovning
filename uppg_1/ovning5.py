#Kod jag hittade på wiki om Power iteration
import numpy as np
import numpy.linalg as LA

def Rayleigh_quotien(B, b):
    b_t = np.transpose(b) 
    quot = np.dot(b_t, (np.dot(B, b)))
    return quot

def power_iteration(B, p):
    # Ideally choose a random vector
    # To decrease the chance that our vector
    # Is orthogonal to the eigenvector
    b_k = np.random.rand(B.shape[1])
    prev_λ = 0;
    err = np.inf
    while err > (10**(-p)):
        # calculate the matrix-by-vector product Ab
        b_k1 = np.dot(B, b_k)

        # calculate the norm
        b_k1_norm = LA.norm(b_k1)

        # re normalize the vector
        b_k = b_k1 / b_k1_norm
        λ = Rayleigh_quotien(B, b_k)
        err = np.abs(prev_λ - λ)
        prev_λ = λ

    return prev_λ, b_k



def uppgiftA():
    B = np.array([[9, 5],
                  [1, 5]])
    p = 5; 
    #Våran kod beräkning
    max_value, vector = power_iteration(B, p)
    #LA.eig beräkning
    eig_values, vectors = LA.eig(B)
    max_eig_value = np.max(np.abs(eig_values))
    print(f"Uppgift A\nTestar våran kod och jämnför resultatet med det vi får från LA.eig()\nB = {B}\np = {p}\nVåran kod ger: {max_value}\n(LA.eig() returnerar i sig själv lista med egenvärden och en lista med egenvektorer, men vi söker bara största egenvärdet,vilket är det som vissas här)\nLA.eig ger: {max_eig_value}\nResultaten blir att:\t Våran kod = LA.eig : {max_eig_value==max_value}")

def uppgiftB():
    A = np.array(np.random.randint(low = -10, high = 10, size = (500, 500)))
    B = A + np.transpose(A)
    p = 5
    λ, v = power_iteration(B, p)
    lenght = ((np.dot(B, v)) - (np.dot(λ, v)))
    print(f"Uppgift B\nB = A + A^t\t500x500-matris\np = {p}\nstörsta egenvärdet λ = {λ}\nmotsvarande egenvektor v = {v}\nBv − λv = {LA.norm(lenght)}")
    
if __name__ == "__main__":
    uppgiftA()
    uppgiftB()