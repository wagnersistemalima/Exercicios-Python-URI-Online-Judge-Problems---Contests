#Ex1118 Várias notas com validação
hipotese = True
while hipotese:
    primeira_nota = float(input())
    while primeira_nota < 0 or primeira_nota > 10:
        print('nota invalida')
        primeira_nota = float(input())
    segunda_nota = float(input())
    while segunda_nota < 0 or segunda_nota > 10:
        print('nota invalida')
        segunda_nota = float(input())
    media = (primeira_nota + segunda_nota) / 2
    print('media = {:.2f}'.format(media))
    print('novo calculo (1-sim 2-nao)')
    opcao = float(input())
    while opcao < 1 or opcao > 2:
        print('novo calculo (1-sim 2-nao)')
        opcao = float(input())
    if opcao == 2:
        hipotese = False







