#Ex1010  Cálculo Simples 09/04/2020
entrada1 = input().split()
entrada2 = input().split()
codigo1, quantidade1, valor1 = entrada1
codigo2, quantidade2, valor2 = entrada2
codigo1 = int(codigo1)
quantidade1 = int(quantidade1)
valor1 = float(valor1)
codigo2 = int(codigo2)
quantidade2 = int(quantidade2)
valor2 = float(valor2)
valor_pagar = quantidade1 * valor1 + quantidade2 * valor2
print('VALOR A PAGAR: R$ {:.2f}'.format(valor_pagar))
