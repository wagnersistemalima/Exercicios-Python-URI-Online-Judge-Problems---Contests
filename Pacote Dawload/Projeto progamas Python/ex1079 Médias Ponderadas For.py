casos = int(input())
peso1 = 2
peso2 = 3
peso3 = 5
soma_pesos = peso1 + peso2 + peso3
for c in range(1, casos + 1):
    valor1, valor2, valor3 = map(float, input().split())
    media_ponderada = ((valor1 * peso1) + (valor2 * peso2) + (valor3 * peso3)) / soma_pesos
    print('{:.1f}'.format(media_ponderada))