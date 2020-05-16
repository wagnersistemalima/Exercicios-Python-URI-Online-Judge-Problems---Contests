#ex1018 Cédulas 09/04/2020
entrada = int(input())
cem = entrada // 100
print('{} nota(s) de R$ 100,00'.format(cem))
cinquenta = (entrada % 100) // 50
print('{} nota(s) de R$ 50,00'.format(cinquenta))
vinte = (entrada % 100) % 50 // 20
print('{} nota(s) de R$ 20,00'.format(vinte))
dez = ((entrada % 100) % 50 % 20) // 10
print('{} nota(s) de R$ 10,00'.format(dez))
cinco = ((entrada % 100) % 50 % 20 % 10) // 5
print('{} nota(s) de R$ 5,00'.format(cinco))
dois = ((entrada % 100) % 50 % 20 % 10 % 5) // 2
print('{} nota(s) de R$ 2,00'.format(dois))







