notas = [""]*5
soma = acima = 0
for x in range (len(notas)):
    notas[x] = float(input(f"Informe a {x+1}ª nota: "))
    soma += notas[x]
media = soma/len(notas)
for y in range (len(notas)):
    if notas[y] > media:
        acima += 1
print (f"A média foi {media:.1f} e houveram {acima} alunos acima da media")