#1131 Grenais
cont = cont_inter = cont_gremio = cont_empate = 0
while True:
    inter, gremio = map(int, input().split())
    print('Novo grenal (1-sim 2-nao)')
    opcao = int(input())
    cont = cont + 1
    if inter > gremio:
        cont_inter = cont_inter + 1
    elif gremio > inter:
        cont_gremio = cont_gremio + 1
    if inter == gremio:
        cont_empate = cont_empate + 1

    while opcao < 1 or opcao > 2:
        print('Novo grenal (1-sim 2-nao)')
        opcao = int(input())
    if opcao == 2:
        print('{} grenais'.format(cont))
        print('Inter:{}'.format(cont_inter))
        print('Gremio:{}'.format(cont_gremio))
        print('Empates:{}'.format(cont_empate))
        if cont_inter > cont_gremio:
            print('Inter venceu mais')
        elif cont_gremio > cont_inter:
            print('Gremio venceu mais')
        break
