nomes = [""]*5
senhas = [""]*5
for x in range (len(nomes)):
    nomes[x] = input("Informe seu nome: ")
    senhas[x] = int(input("Informe sua senha: "))
for z in range (5):
    print (f"Usuário: {nomes[z]}, senha: {senhas[z]}")