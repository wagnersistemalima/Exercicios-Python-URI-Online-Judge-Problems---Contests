#1020 Idade em dias 09/04/2020
idade_dias = int(input())
anos = idade_dias // 365
meses = (idade_dias % 365) // 30
dias = (idade_dias % 365) % 30
print('{} ano(s)'.format(anos))
print('{} mes(es)'.format(meses))
print('{} dia(s)'.format(dias))