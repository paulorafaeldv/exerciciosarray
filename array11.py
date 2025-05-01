"""Escreva um algoritmo que solicite ao
usuário a entrada de 5 nomes, e que exiba
a lista desses nomes na tela.
Após exibir essa lista, o programa deve
mostrar também os nomes na ordem
inversa em que o usuário os digitou, um
por linha."""

nomes = [""]*5
for x in range (len(nomes)):
    nomes[x] = input("Informe um nome: ")
print (nomes)
for x in range (len(nomes)-1, -1, -1):
    print (nomes[x])