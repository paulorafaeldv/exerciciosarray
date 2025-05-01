import random

# Palavra secreta
palavra_secreta = "abacate"

# Número de tentativas
tentativas = 6

# Letras acertadas
letras_acertadas = ["_"] * len(palavra_secreta)

while tentativas > 0 and "_" in letras_acertadas:
    # Imprime a palavra com as letras acertadas
    print(" ".join(letras_acertadas))

    # Imprime o boneco da forca
    if tentativas == 6:
        print("----------")
        print("|        |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("_|__ _")
    elif tentativas == 5:
        print("----------")
        print("|        |")
        print("|        O")
        print("|")
        print("|")
        print("|")
        print("_|__ _")
    elif tentativas == 4:
        print("----------")
        print("|        |")
        print("|        O")
        print("|        |")
        print("|")
        print("|")
        print("_|__ _")
    elif tentativas == 3:
        print("----------")
        print("|        |")
        print("|        O")
        print("|       /|")
        print("|")
        print("|")
        print("_|__ _")
    elif tentativas == 2:
        print("----------")
        print("|        |")
        print("|        O")
        print("|       /|\\")
        print("|")
        print("|")
        print("_|__ _")
    elif tentativas == 1:
        print("----------")
        print("|        |")
        print("|        O")
        print("|       /|\\")
        print("|       /")
        print("|")
        print("_|__ _")

    # Pede ao usuário que digite uma letra
    letra = input("Digite uma letra: ").lower()

    # Verifica se a letra está na palavra secreta
    if letra in palavra_secreta:
        for i, l in enumerate(palavra_secreta):
            if l == letra:
                letras_acertadas[i] = letra
    else:
        tentativas -= 1
        print(f"Você errou! Restam {tentativas} tentativas.")

# Verifica se o usuário ganhou ou perdeu
if "_" not in letras_acertadas:
    print(" ".join(letras_acertadas))
    print("Parabéns! Você ganhou!")
else:
    print("----------")
    print("|        |")
    print("|        O")
    print("|       /|\\")
    print("|       / \\")
    print("|")
    print("_|__ _")
    print(f"A palavra secreta era {palavra_secreta}. Você perdeu!")
