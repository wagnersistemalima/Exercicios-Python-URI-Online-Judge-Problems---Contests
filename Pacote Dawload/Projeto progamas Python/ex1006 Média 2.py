#Ex1006 Média 2 09/04/2020
nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
peso1 = 2
peso2 = 3
peso3 = 5
soma_peso = peso1 + peso2 + peso3
media = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / soma_peso
print('MEDIA = {:.1f}'.format(media))