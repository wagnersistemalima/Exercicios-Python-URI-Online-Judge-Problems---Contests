#Ex1070 Seis Números Impares
entrada = int(input())
numero = entrada
fim = entrada + 12
while numero <= fim:
    if numero % 2 == 1:
        print(numero)
    numero = numero + 1
