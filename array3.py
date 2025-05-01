nomes = ["ana", "jose", "caio"]
usuario = input("Pesquise o nome: ")
for x in range (len(nomes)):
    if usuario in nomes[x]:
        print (f"Usuario encontrado na posição {x}")
