import numpy as np


class Vector:

    def __init__(self, vector1, vector2):
        self.v1 = vector1
        self.v2 = vector2

    def riktadevectorer(self, v1, v2):
        summa = []
        self.v1.split()
        self.v2.split()
        for i in range(self.v1):
            summa.append((self.v1[i]*self.v2[i])/(self.v2[i]**2))
        #for-loopen går igenom varje skalär i de två vektrorerna och utför projektionens ekvation
        return summa
    

def interaction():
    # Här kollar vi vad de tänker skriva in så att programmet inte klagar
    svar = input("Tänker du använda två riktningsvektorer eller en normalvector? Tryck 1 för normalvecktor och 2 för riktningsvektorer. ")
    print (svar)

    if svar == "1":
        nyVector = input("Skriv in din normalvector: ")
        pass

    elif svar == "2":
        Vector1 = input("Skriv in din första vector: ")
        Vector2 = input("Skriv in din andra vector: ")
        projektor = Vector(Vector1, Vector2)
        projektor.riktadevectorer(Vector1, Vector2)

    else:
        print("Du valde inte rätt, hejdå!")


if __name__ == "__main__":
    interaction()

