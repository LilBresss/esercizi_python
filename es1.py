tupla_competizioni = (
    ("ChefA", "Piatto1", 8.5, 5),
    ("ChefB", "Piatto2", 7.2, 4),
    ("ChefC", "Piatto3", 9.0, 6),
    ("ChefA", "Piatto4", 7.8, 5),
    ("ChefB", "Piatto5", 8.1, 4),
    ("ChefC", "Piatto6", 8.9, 7)
)

#1
def media_punteggio_competizioni(tupla_competizioni):
    media = 0
    for (chef, piatto, punteggio, nGiudici) in tupla_competizioni:
        media += punteggio
    return media/len(tupla_competizioni)

#2
def media_punteggio_chef(tupla_competizioni, chef):
    media = 0
    nPunt = 0
    for (chefTupla, piatto, punteggio, nGiudici) in tupla_competizioni:
        if(chef == chefTupla):
            media += punteggio
            nPunt += 1
    return media/nPunt

#3
def competizione_con_piu_giudici(tupla_competizioni):
    max = 0
    for (chef, piatto, punteggio, nGiudici) in tupla_competizioni:
        if(nGiudici > max):
            max = nGiudici

    listaMax = []
    for (chef, piatto, punteggio, nGiudici) in tupla_competizioni:
        if(nGiudici == max):
            listaMax.append((chef, piatto, punteggio, nGiudici))
    
    return listaMax

#4
def competizione_con_meno_giudici(tupla_competizioni):
    min = tupla_competizioni[0][3]
    for (chef, piatto, punteggio, nGiudici) in tupla_competizioni:
        if(nGiudici < min):
            min = nGiudici

    listaMin = []
    for (chef, piatto, punteggio, nGiudici) in tupla_competizioni:
        if(nGiudici == min):
            listaMin.append((chef, piatto, punteggio, nGiudici))
    
    return listaMin


ciclo = True
while ciclo:
    print("1 - Media punteggio competizioni")
    print("2 - Media punteggio di uno chef specifico")
    print("3 - La competizione con più giudici")
    print("4 - La competizione con meno giudici")
    print("0 - Esci")           
    indice = int(input("selezione la funzione da svolgere: "))        

    if(indice == 1):
        media = media_punteggio_competizioni(tupla_competizioni)
        print(f"media generale: {media}")
    elif(indice == 2):
        ciclo1 = True
        while ciclo1:
            chef = str(input("inserisci il nome dello chef di cui calcolare la media: "))
            for (chefTupla, piatto, punteggio, nGiudici) in tupla_competizioni:
                if(chef == chefTupla):
                    ciclo1 = False
                    break
            if ciclo:
                print("errore! chef non trovato")

        mediaChef = media_punteggio_chef(tupla_competizioni, chef)

        print(f"media dello chef {chef}: {mediaChef}")
    elif(indice == 3):
        listaMax = competizione_con_piu_giudici(tupla_competizioni)
        print("competizione con il maggior numero di giudici:",listaMax)
    elif(indice == 4):
        listaMin = competizione_con_meno_giudici(tupla_competizioni)
        print("competizione con il minor numero di giudici:",listaMin)
    elif(indice == 0):
        ciclo = False
    else:
        print("errore! indice inserito sbagliato")