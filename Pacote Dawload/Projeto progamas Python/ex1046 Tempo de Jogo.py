#Ex1046 Tempo de Jogo 10/04/2020
hora_inicial, hora_final = map(int, input().split())
if hora_inicial == hora_final:
    duracao = 24
    print('O JOGO DUROU {} HORA(S)'.format(duracao))
elif hora_inicial < hora_final:
    duracao = hora_final - hora_inicial
    print('O JOGO DUROU {} HORA(S)'.format(duracao))
if hora_inicial > hora_final:
    duracao = (24 - hora_inicial) + hora_final
    print('O JOGO DUROU {} HORA(S)'.format(duracao))
