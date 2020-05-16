#Ex 1080 Maior e Posição.
maior = 0
menor = 0
posicao = 0
for c in range(1, 101):
    valor = int(input())
    if c == 1:     # comecei a analizar a partir do primeiro valor
        maior = valor
        menor = valor
        posicao = c
    else:
        if valor > maior:
            maior = valor
            posicao = c
        if valor < menor:
            menor = valor
print('{}'.format(maior))
print('{}'.format(posicao))





