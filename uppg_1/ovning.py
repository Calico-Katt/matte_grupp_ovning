import numpy as np


#Kör från minet just nu, så formlen kan behövas göras om en del

def projektion(u, v): 
    vector=[]
    for i in range(u):
        vector=u[i]*v[i]