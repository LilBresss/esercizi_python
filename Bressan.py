import random

# 1)
dizionario = {
    "Mario Rossi":[("Antipasti",(8,7,9),"Junior Chef"),("Primi",(7,8,8),"Junior Chef"),("Secondi",(9,9,8),"Junior Chef"),("Dessert",(8,8,9),"Junior Chef")],
    "Luigi Bianchi":[("Antipasti",(7,7,8),"Senior Chef"),("Primi",(8,9,7),"Senior Chef"),("Secondi",(7,8,7),"Senior Chef"),("Dessert",(9,8,8),"Senior Chef")],
    "Giulia Verdi":[("Antipasti",(9,8,8),"Junior Chef"),("Primi",(8,7,9),"Junior Chef"),("Secondi",(8,8,8),"Junior Chef"),("Dessert",(7,9,8),"Junior Chef")]
}

# 2)
dizionario["Bressan Simone"] = [("Antipasti",(9,7,8),"Senior Chef"),("Primi",(8,5,8),"Senior Chef"),("Secondi",(8,8,9),"Senior Chef"),("Dessert",(9,9,9),"Senior Chef")]

# 3)
def aggiungiCategoria():
    for nome in dizionario.keys():
        for categ, punteggi, chef in dizionario[nome]:
            categoriaChef = chef
            n1 = random.randint(1,10)
            n2 = random.randint(1,10)
            n3 = random.randint(1,10)
            tupla = (n1,n2,n3)
            dizionario[nome].append(("Piatti unici", tupla, categoriaChef))
            break

# 4)
def ricercaChef(nome):
    if(nome in dizionario.keys()):
        print(f"\nCognome e Nome: {nome}")
        for categ, punteggi, chef in dizionario[nome]:
            print(f"Categoria di Chef: {chef}\n")
            break
        for categ, punteggi, chef in dizionario[nome]:
            print(f"Punteggi {categ}: {punteggi}\n   creatività: {punteggi[0]}\n   gusto: {punteggi[1]}\n   presentazione: {punteggi[2]}\n")
    else:
        print("ERRORE! chef inesistente")

# 5)
def ricercaPiatto(piatto):
    presenza = False
    print(f"\nPiatto: {piatto}\n")
    for nome in dizionario.keys():
        for categ, punteggi, chef in dizionario[nome]:
            if(categ == piatto):
                print(f"Cognome e Nome: {nome}\nPunteggi: {punteggi}\n   creatività: {punteggi[0]}\n   gusto: {punteggi[1]}\n   presentazione: {punteggi[2]}\n")
                pesenza = True
    if(presenza == False):
        print("ERRORE! piatto inesistente")

# 6)
def stampaPunteggioMax(dizionario, piatto, catChef):
    presenza = False
    max = 0
    chefMax = []
    for nome in dizionario.keys():
        for categ, punteggi, chef in dizionario[nome]:
            if(categ == piatto and chef == catChef):
                punteggio = punteggi[0] + punteggi[1] + punteggi[2]
                if(punteggio > max):
                    max = punteggio
                presenza = True

    for nome in dizionario.keys():
        for categ, punteggi, chef in dizionario[nome]:
            if(categ == piatto and chef == catChef):
                punteggio = punteggi[0] + punteggi[1] + punteggi[2]
                if(punteggio == max):
                    chefMax.append(nome)
    if(presenza):
        print(f"Chef che hanno raggiunto il punteggio massimo di {max}: {chefMax}")
    if(presenza == False):
        print("ERRORE! valori inesistenti")

# 7)
def inserisci_dati_nuovo_chef():
    validita =  False

    categoriePiatti = ["Antipasti", "Primi", "Secondi", "Dessert", "Piatti unici"]

    risultati = []

    nome = input("inserisci il nome dello chef: ")
    cognome = input("inserisci il cognome dello chef: ")
    nominativo = (nome, cognome)

    categoriaChef = input("inserisci la categoria dello chef: ")
    
    for i in range(len(categoriePiatti)):
        print(f"inserisci i punteggi per la categoria {categoriePiatti[i]}: ")
        n1 = int(input("inserisci il punteggio per la creatività: "))
        n2 = int(input("inserisci il punteggio per il gusto: "))
        n3 = int(input("inserisci il punteggio per la presentazione: "))
        punteggi = (n1,n2,n3)
        tupla= (categoriePiatti[i],punteggi,categoriaChef)
        if(len(nominativo) and len(tupla) == 3):
            validita = True
            risultati.append(tupla)

    return validita, nominativo,risultati

def inserisci_nuovo_chef(dizionario, nominativo, risultati, validita):
    if(validita):
        dizionario[nominativo] = risultati
    else:
        print("ERRORE! valori inesistenti")

validita,nominativo, risultati = inserisci_dati_nuovo_chef()
inserisci_nuovo_chef(dizionario, nominativo, risultati, validita)