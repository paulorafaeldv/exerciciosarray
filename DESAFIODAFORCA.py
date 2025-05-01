p = "coiote".upper()
palavra = ["_"] * len(p)
erro = 0
def forca():
    if erro == 0:
        print("----------"
              "\n|        |"
              "\n|        "
              "\n|        "
              "\n|        "
              "\n|__      ", " ".join(palavra)) #separei a variavel palavra para ir adicionando as letras

    elif erro == 1:
        print("----------"
              "\n|        |"
              "\n|        O"
              "\n|        "
              "\n|        "
              "\n|__      ", " ".join(palavra))
    elif erro == 2:
        print("----------"
              "\n|        |"
              "\n|        O"
              "\n|        |"
              "\n|        "
              "\n|__      ", " ".join(palavra))
    elif erro == 3:
        print("----------"
              "\n|        |"
              "\n|        O"
              "\n|        |"
              "\n|       /"
              "\n|__      ", " ".join(palavra))
    elif erro == 4:
        print("----------"
              "\n|        |"
              "\n|        O"
              "\n|        |"
              "\n|       / \ "
              "\n|__      ", " ".join(palavra))
    elif erro == 5:
        print("----------"
              "\n|        |"
              "\n|        O"
              "\n|       /|"
              "\n|       / \ "
              "\n|__      ", " ".join(palavra))
    elif erro == 6:
        print("----------"
              "\n|        |"
              "\n|        O"
              "\n|       /|\ "
              "\n|       / \ "
              "\n|__      ", " ".join(palavra))
        print()
print ("-"*30)
print ("JOGO DA FORCA")
print ("-"*30)
forca()
print ()
tentativas = 0
while tentativas < 6:
    letra = input("Digite uma letra: ").upper()
    if letra in p:
        for x in range (len(p)):
            if letra == p[x]:
                palavra[x] = letra
        forca()
    if letra not in p:
        print(f"Não tem {letra}! Tente novamente.")
        erro += 1
        forca()
    tentativas += 1
if erro < 5:
    palpite = input("Hora de arriscar! Digite a palavra: ").upper()
    if palpite == p:
        print("PARABENS! Você ganhou!!")
    else:
        print(f"Você perdeu :( a palavra era {p}")
if erro >= 5:
    print(f"Você perdeu :( a palavra era {p}")
