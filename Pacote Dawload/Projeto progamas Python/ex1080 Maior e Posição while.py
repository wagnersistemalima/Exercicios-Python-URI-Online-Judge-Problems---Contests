# EX1080 Maior e posição while
cont = 0
maior = 0
posicao = 0
while cont < 100:
    cont = cont + 1
    valor = int(input())
    if cont == 1:
        maior = valor
        posicao = cont
    else:
        if valor > maior:
            maior = valor
            posicao = cont
print(maior)
print(posicao)
