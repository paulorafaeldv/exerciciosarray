"""Faça um código para ler um valor N qualquer (que será o
tamanho dos vetores). Após, ler dois
vetores A e B (de tamanho N cada um) e depois
armazenar em um terceiro vetor Soma a soma dos
elementos do vetor A com os do vetor B (respeitando as
mesmas posições) e escrever o vetor Soma."""

N = int(input("Informe o tamanho dos vetores: "))
A = [""]*N
for x in range (N):
    A[x] = int(input("Informe um valor para o vetor 1: "))
B = [""]*N
for y in range (N):
    B[y] = int(input("Informe um valor para o vetor 2: "))
C = [""]*N
for z in range (N):
    C[z] = A[z] + B[z]
print(C)