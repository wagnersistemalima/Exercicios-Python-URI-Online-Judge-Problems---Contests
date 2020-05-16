#Ex1009 Salário com Bônus 09/04/2020
vendedor = str(input())
salario = float(input())
venda_mes = float(input())
comissao = venda_mes * (15 / 100)
total_salario = salario + comissao
print('TOTAL = R$ {:.2f}'.format(total_salario))