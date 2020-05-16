# ex1134 Tipo de combustivel while

sair = False
clientes = 1
cont_alcool = cont_gasolina = cont_disel = 0
while not sair:
    pergunta = int(input())

    if pergunta == 1:
        cont_alcool = cont_alcool + 1
    elif pergunta == 2:
        cont_gasolina = cont_gasolina + 1
    if pergunta == 3:
        cont_disel = cont_disel + 1
    if pergunta == 4:
        sair = True
print('MUITO OBRIGADO')
print('Alcool: {}'.format(cont_alcool))
print('Gasolina: {}'.format(cont_gasolina))
print('Diesel: {}'.format(cont_disel))







