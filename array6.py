numeros = [""]*5
for x in range (len(numeros)):
    numeros[x] = int(input("Digite um número: "))
print (numeros)
for y in range (len(numeros)-1, -1, -1):
    print (numeros[y], end = " ")