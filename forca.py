p = "wellington".upper()
palavra = ["_"] * len(p)
erro = 0

def forca():
    if erro == 0:
        print("----------")
        print("|        |")
        print("| ")
        print("| ")
        print("| ")
        print("|__ ")
        for x in palavra:
            print(x, end=" ")
    elif erro == 1:
        print("----------")
        print("|        |")
        print("|        O")
        print("| ")
        print("| ")
        print("|__ ")
        for x in palavra:
            print(x, end=" ")
    elif erro == 2:
        print("----------")
        print("|        |")
        print("|        O")
        print("|        |")
        print("| ")
        print("|__ ")
        for x in palavra:
            print(x, end=" ")
    elif erro == 3:
        print("----------")
        print("|        |")
        print("|        O")
        print("|        |")
        print("|       /")
        print("|__ ")
        for x in palavra:
            print(x, end=" ")
    elif erro == 4:
        print("----------")
        print("|        |")
        print("|        O")
        print("|        |")
        print("|       / \ ")
        print("|__ ")
        for x in palavra:
            print(x, end=" ")
    elif erro == 5:
        print("----------")
        print("|        |")
        print("|        O")
        print("|       /|")
        print("|       / \ ")
        print("|__ ")
        for x in palavra:
            print(x, end=" ")
    elif erro == 6:
        print("----------")
        print("|        |")
        print("| O")
        print("| /|\\")
        print("| / \\")
        print("|__ ")
        for x in palavra:
            print(x, end=" ")
    print()

print("-"*30)
print("JOGO DA FORCA")
print("-"*30)
forca()
print()

tentativas = 0
while tentativas < 6:
    letra = input("Digite uma letra: ").upper()
    if letra in p:
        for x in range(len(p)):
            if letra == p[x]:
                palavra[x] = letra
        forca()
    if letra not in p:
        print(f"Não tem {letra}! Tente novamente.")
        erro += 1
        forca()
    tentativas += 1
    if "_" not in palavra:
        print("PARABENS! Você ganhou!!")
        break

if erro < 5:
    palpite = input("Hora de arriscar! Digite a palavra: ").upper()
    if palpite == p:
        print("PARABENS! Você ganhou!!")
    else:
        print(f"Você perdeu :( a palavra era {p}")
if erro >= 5:
    print(f"Você perdeu :( a palavra era {p}")