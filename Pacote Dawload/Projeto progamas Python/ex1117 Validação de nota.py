#Ex 1117 validação de nota.
casos = 0
soma = media = 0
while casos != 2:
    nota = float(input())
    if nota >= 0 and nota <= 10:
        soma = soma + nota
        media = soma / 2
        casos = casos + 1
    else:
        print('nota invalida')
print('media = {}'.format(media))

