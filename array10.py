"""Faça um código para ler 10 números e
guardar num vetor. Após isto, ler mais um
número qualquer, calcular e escrever
quantas vezes esse número aparece no
vetor."""

from time import sleep
v = [""]*10
for x in range (len(v)):
    v[x] = int(input("Informe um número: "))
print()
print (v)
print()
sleep(1)
n = int(input("Pesquise um número: "))
enc = 0
for x in range (len(v)):
    if v[x] == n:
        enc = 1
        print (f"Encontrado na posição {x+1}")
if enc == 0:
    print("Número não encontrado")