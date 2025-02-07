import numpy as np


class Vector:

    def __init__(self, vector1, vector2, normalvector):
        self.v1 = vector1
        self.v2 = vector2
        self.nv = normalvector
    

def interaction():
    #Här kollar vi vad de tänker skriva in så att programmet inte klagar
    svar = input("Tänker du använda två riktningsvektorer eller en normalvector? Tryck 1 för normalvecktor och 2 för riktningsvektorer.")
    print (svar)

    if svar == 1:
        nyVector=input("Skriv in din normalvector")
        pass

    elif svar == 2:
        Vector1=input("Skriv in din första vector")
        Vector2 = input("Skriv in din andra vector")
        pass

    else:
        print("Du valde inte rätt, hejdå!")


if __name__ == "__main__":
    pass

