tupla_produzione_agricola = (
    ("Toscana", [
        ("gennaio", ("grano", 1200)),
        ("gennaio", ("mais", 1000)),
        ("febbraio", ("grano", 1100)),
        ("febbraio", ("mais", 950)),
        ("marzo", ("grano", 1000)),
        ("marzo", ("mais", 850)),
        ("aprile", ("grano", 900)),
        ("aprile", ("mais", 850)),
        ("maggio", ("grano", 1300)),
        ("maggio", ("mais", 800)),
        ("giugno", ("grano", 1260)),
        ("giugno", ("mais", 1000))
    ]),
    ("Lombardia", [
        ("gennaio", ("grano", 1300)),
        ("gennaio", ("mais", 850)),
        ("febbraio", ("grano", 1250)),
        ("febbraio", ("mais", 920)),
        ("marzo", ("grano", 1200)),
        ("marzo", ("mais", 900)),
        ("aprile", ("grano", 1150)),
        ("aprile", ("mais", 850)),
        ("maggio", ("grano", 1100)),
        ("maggio", ("mais", 870)),
        ("giugno", ("grano", 1050)),
        ("giugno", ("mais", 970))
    ]),
    ("Campania", [
        ("gennaio", ("grano", 1100)),
        ("gennaio", ("mais", 980)),
        ("febbraio", ("grano", 1150)),
        ("febbraio", ("mais", 1020)),
        ("marzo", ("grano", 1200)),
        ("marzo", ("mais", 950)),
        ("aprile", ("grano", 1250)),
        ("aprile", ("mais", 820)),
        ("maggio", ("grano", 1300)),
        ("maggio", ("mais", 870)),
        ("giugno", ("grano", 1150)),
        ("giugno", ("mais", 850))
    ])
)

def analizza_produzione_agricola(tupla_produzione_agricola, regione_produzione_agricola, tipo_produzione_agricola):
    lista = []

    media_produzione = 0
    max_produzione = 0
    
    nProduzione = 0
    for regione, produzione in tupla_produzione_agricola:
        for mese, prod in produzione:
            if(regione_produzione_agricola == regione and prod[0] == tipo_produzione_agricola):
                media_produzione += prod[1]
                nProduzione += 1
    media_produzione = media_produzione/nProduzione

    lista.append(media_produzione)

    for regione, produzione in tupla_produzione_agricola:
        for mese, prod in produzione:
            if(regione_produzione_agricola == regione and prod[0] == tipo_produzione_agricola and prod[1] > max_produzione):
                max_produzione = prod[1]


    for regione, produzione in tupla_produzione_agricola:
        for mese, prod in produzione:
            if(regione_produzione_agricola == regione and prod[0] == tipo_produzione_agricola and prod[1] == max_produzione):
                lista.append((prod[1], mese))

    return lista

risultato = analizza_produzione_agricola(tupla_produzione_agricola, "Toscana", "mais")
print("Risultato per 'Toscana' e 'mais':", risultato)

risultato = analizza_produzione_agricola(tupla_produzione_agricola, "Lombardia", "grano")
print("Risultato per 'Lombardia' e 'grano':", risultato)

risultato = analizza_produzione_agricola(tupla_produzione_agricola, "Campania", "mais")
print("Risultato per 'Campania' e 'mais':", risultato)