#1079 Médias Ponderadas usando while
casos = int(input())
cont = 1
peso_valor1 = 2
peso_valor2 = 3
peso_valor3 = 5
soma_pesos = peso_valor1 + peso_valor2 + peso_valor3
while cont <= casos:
    valor1, valor2, valor3 = map(float, input().split())
    media = ((valor1 * peso_valor1) + (valor2 * peso_valor2) + (valor3 * peso_valor3)) / soma_pesos
    print('{:.1f}'.format(media))
    cont = cont + 1