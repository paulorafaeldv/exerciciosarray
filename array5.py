"""preencher um vetor A com 10 números. logo em
seguida, ler mais um número e guardar em uma
variável X.
Armazenar em um vetor M o resultado de cada elemento
de A multiplicado pelo valor X.
no final imprimir o vetor M."""

a = [1,2,3,4,5,6,7,8,9,10]
m = [""]*10
x = int(input("Informe um multiplicador: "))
for y in range (len(m)):
    m[y] = x * a[y]
print (m)