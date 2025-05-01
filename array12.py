"""Faça um algoritmo que leia 10 valores do tipo
inteiro e armazene-os em um vetor.
A seguir, o algoritmo deverá informar
(1) todos os números pares que existem no
vetor;
(2) o menor e o maior valor existente no vetor;
(3) quantos dos valores do vetor são maiores
que a média desses valores:"""

vetor = [0]*10
for x in range (len(vetor)):
    vetor[x] = int(input("Informe um número inteiro: "))
print ("Números pares: ")
for x in range (len(vetor)):
    if vetor[x] % 2 == 0:
        print (vetor[x], end = " ")
maior = menor = cont = 0
for x in range (len(vetor)):
    cont += 1
    if cont == 1:
        maior = vetor[x]
        menor = vetor[x]
    if vetor [x] > maior:
        maior = vetor[x]
    elif vetor [x] < menor:
        menor = vetor[x]
print(f"\nO maior número é {maior} e o menor número é {menor}")
soma = 0
for x in range (len(vetor)):
    soma += vetor[x]
media = soma/len(vetor)
print (f"A média é {media:.1f}")
print ("Os valores acima da média são: ")
for x in range (len(vetor)):
    if vetor[x] > media:
        print (vetor[x], end = " ")