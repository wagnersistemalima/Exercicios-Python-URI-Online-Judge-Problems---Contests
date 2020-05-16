#Ex 1094 Experiências
quantidade_casos = int(input())
soma_total = soma_r = soma_s = soma_c = 0
for c in range(1, quantidade_casos + 1):
    caso = input().upper().strip().split()
    numero = int(caso[0])
    letra = str(caso[1])
    soma_total = soma_total + numero
    if letra == 'R':
        soma_r = soma_r + numero
    if letra == 'S':
        soma_s = soma_s + numero
    if letra == 'C':
        soma_c = soma_c + numero
percentual_coelho = (soma_c / soma_total) * 100
percentual_rato = (soma_r / soma_total) * 100
percentual_sapo = (soma_s / soma_total) * 100
print('Total: {} cobaias'.format(soma_total))
print('Total de coelhos: {}'.format(soma_c))
print('Total de ratos: {}'.format(soma_r))
print('Total de sapos: {}'.format(soma_s))
print('Percentual de coelhos: {:.2f} %'.format(percentual_coelho))
print('Percentual de ratos: {:.2f} %'.format(percentual_rato))
print('Percentual de sapos: {:.2f} %'.format(percentual_sapo))


