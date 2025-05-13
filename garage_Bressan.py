class Macchina:
    def __init__(self, targa, marca, modello, anno):
        """
        Inizializza gli attributi della macchina
        """
        self.targa = targa
        self.marca = marca
        self.modello = modello
        self.anno = anno

    def __str__(self):
        """
        Restituisce una descrizione leggibile della macchina
        """
        return f"{self.marca} {self.modello} ({self.anno}) - Targa: {self.targa}"
    

class Garage:
    def __init__(self):
        """
        Inizializza la lista delle macchine
        """
        self.lista = []

    def aggiungi_macchina(self, macchina):
        """
        Aggiunge una macchina alla lista
        """
        self.lista.append(macchina)
        print("macchina aggiunta con successo")

    def rimuovi_macchina(self, targa):
        """
        Rimuove una macchina in base alla targa
        """
        if(len(self.lista) == 0):
            print("la lista è vuota!")
        else:
            trovato = False

            for i in range(len(self.lista)):
                macchina = self.lista[i]
                if(targa == macchina.targa):
                    self.lista.remove(macchina)
                    print(f"macchina {macchina.marca} {macchina.modello} ({macchina.anno}) rimossa con successo!")
                    trovato = True
            
            if(trovato == False):
                print("macchina non trovata!")

    def elenco_macchine(self):
        """
        Mostra tutte le macchine nel garage
        """
        if(len(self.lista) == 0):
            print("la lista è vuota!")
        else:
            for i in range(len(self.lista)):
                print(f"{self.lista[i]}")

    def cerca_macchina(self, targa):
        """
        Cerca e restituisce le informazioni di una macchina tramite la targa
        """
        if(len(self.lista) == 0):
            print("la lista è vuota!")
        else:
            trovato = False
            
            for i in range(len(self.lista)):
                if(targa == self.lista[i].targa):
                    print(f"{self.lista[i]}")
                    trovato = True
            
            if(trovato == False):
                print("macchina non presente!")


garage = Garage()

ciclo = True

while(ciclo):
    print("menu: ")
    print("1) aggiungi macchina")
    print("2) rimuovi macchina")
    print("3) elenco macchine")
    print("4) cerca macchina")
    print("0) esci")
    scelta = int(input("scegli: "))

    if(scelta == 0):
        print("\narrivederci!")
        ciclo = False
    elif(scelta == 1):
        print()
        targa = str(input("inserisci la targa: "))
        marca = str(input("inserisci la marca: "))
        modello = str(input("inserisci il modello: "))
        anno = 0
        while(anno <= 0):
            anno = int(input("inserisci l'anno: "))
            if(anno <= 0):
                print("l'anno deve essere maggiore di 0")
        macchina = Macchina(targa, marca, modello, anno)
        garage.aggiungi_macchina(macchina)
    elif(scelta == 2):
        targa = str(input("\ninserisci la targa del veicolo da rimuovere: "))
        print("rimozione della macchina con targa",targa)
        garage.rimuovi_macchina(targa)
    elif(scelta == 3):
        print("\nmacchine presenti nel garage:")
        garage.elenco_macchine()
    elif(scelta == 4):
        targa = str(input("\ninserisci la targa del veicolo da cercare: "))
        print("ricerca della macchina con targa",targa)
        garage.cerca_macchina(targa)        
    else:
        print("\nscelta inserita non valida!")

    print("\n----------------------------------------------------------\n")