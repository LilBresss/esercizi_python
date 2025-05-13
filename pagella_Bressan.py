import math

class Pagella:
    def __init__(self, lista):
        self.pagella = lista

    def __repr__(self):
        return f"{self.pagella}"
    
    def media(self):
        media = 0

        for i in range(len(self.pagella)):
            media += self.pagella[i]

        return media/len(self.pagella)
    
    def __getitem__(self, indice):
        return self.pagella[indice]
    
    def __eq__(self, altra):
        if(len(self.pagella) == len(altra)):
            uguali = []

            for i in range(len(self.pagella)):
                if(self.pagella[i] == altra[i]):
                    uguali.append(True)
                else:
                    uguali.append(False)
            
            if(False in uguali):
                return False
            else:
                return True
        else:
            print("le pagelle hanno diverse dimensioni")
            return False
    
    def __sub__(self, altra):
        if(len(self.pagella) == len(altra)):
            uguali = []

            for i in range(len(self.pagella)):
                uguali.append(self.pagella[0][i] - altra[0][i])
            
            return uguali
        else:
            print("le pagelle hanno diverse dimensioni")
            return None
        
    def impegno(self):
        somma = 0
        for i in range(len(self.pagella)):
            somma += self.pagella[i]^2
        
        return math.sqrt(somma)


pagella1 = Pagella([1,2,3,4,5,6,7,8,9])

print(pagella1)

print(pagella1.media())

print(pagella1[1])

pagella2 = Pagella([2,3,4,5,6,7])

pagella3 = Pagella([1,2,3,4,5,6,7,8,9])

pagella4 = Pagella([1,2,3,4,5,6,5,8,9])

if(pagella1 == pagella2):
    print("le pagelle sono uguali")
else:
    print("le pagelle sono diverse")

if(pagella1 == pagella3):
    print("le pagelle sono uguali")
else:
    print("le pagelle sono diverse")

if(pagella1 == pagella4):
    print("le pagelle sono uguali")
else:
    print("le pagelle sono diverse")

print("sottrazione: ", pagella1 - pagella1)

print(pagella1.impegno())