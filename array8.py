nomes = ["ana", "caio", "paulo"]
senhas = ["123", "333", "321"]
nusuario = input("Digite um nome: ")
susuario = input("Digite a senha: ")
login = 0
for x in range (len(nomes)):
    if nomes[x] == nusuario and senhas[x] == susuario:
        login = 1
        print ("Login efetuado")
        break
if login == 0:
    print ("Acesso negado")
tentativas +=1