import math

tupla_meteo = (("Bergamo", [("gennaio", 10), ("febbraio", 0), ("marzo", "N/D"), ("aprile", 13), ("maggio", 14), ("giugno", 15), ("luglio", 16), ("agosto", "N/D"), ("settembre", 18), ("ottobre", 19), ("novembre", 20), ("dicembre", 21)]),
               ("Como", [("gennaio", "N/D"), ("febbraio", 11), ("marzo", 2), ("aprile", 3), ("maggio", 4), ("giugno", 5), ("luglio", 6), ("agosto", "N/D"), ("settembre", 8), ("ottobre", 9), ("novembre", 10), ("dicembre", 11)]),
               ("Milano", [("gennaio", 0), ("febbraio", 20), ("marzo", 19), ("aprile", 18), ("maggio", 17), ("giugno", "N/D"), ("luglio", 15), ("agosto", 14), ("settembre", "N/D"), ("ottobre", 12), ("novembre", 11), ("dicembre", "N/D")]),
               ("Varese", [("gennaio", 10), ("febbraio", "N/D"), ("marzo", 12), ("aprile", 13), ("maggio", 14), ("giugno", 15), ("luglio", 16), ("agosto", "N/D"), ("settembre", 18), ("ottobre", 19), ("novembre", "N/D"), ("dicembre", 21)])
               )

def calcoli(tupla, citta):
    lista = []
    #calcolo media
    media = 0
    nValori = 0
    for provincia, mesi_valori in tupla_meteo:
        if(provincia == citta):
            for mese, valore in mesi_valori:
                if(valore != 0):
                    media += valore
                    nValori += 1
    
    media = media/nValori

    lista.append(media)
            
    #calcolo minimo
    min = 0
    for provincia, mesi_valori in tupla_meteo:
        if(provincia == citta):
            for mese, valore in mesi_valori: 
                if(valore != 0):
                    min = valore
        
    for provincia, mesi_valori in tupla_meteo:
        if(provincia == citta):
            for mese, valore in mesi_valori:
                if(valore < min):
                    if(valore != 0):
                        min = valore

    for provincia, mesi_valori in tupla_meteo:
        if(provincia == citta):
            for mese, valore in mesi_valori:
                    if(valore != 0):
                        if(valore == min):
                            lista.append((mese, valore))

    #calcolo massimo
    max = 0        
    for provincia, mesi_valori in tupla_meteo:
        if(provincia == citta):
            for mese, valore in mesi_valori:
                if(valore != 0):
                    if(valore > max):
                        max = valore

    for provincia, mesi_valori in tupla_meteo:
        if(provincia == citta):
            for mese, valore in mesi_valori:
                if(valore != 0):
                    if(valore == max):
                        lista.append((mese, valore))

    #ritorno la lista dei risultati dei calcoli
    return lista

ciclo = True
while (ciclo):
    citta = str(input("inserisci una città: "))
    for provincia, mesi_valori in tupla_meteo:
        if(provincia == citta):
            ciclo = False
            break

listaValori = calcoli(tupla_meteo, citta)

if(len(listaValori) != 0):
    print("lista calcoli:", listaValori)
else:
    print("impossibile calcolare")