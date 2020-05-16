#Ex 1038 Lanche 10/04/2020
codigo, quantidade = map(int, input().split())
if codigo == 1:
    cachorro_quente = 4.0
    total = cachorro_quente * quantidade
    print('Total: R$ {:.2f}'.format(total))
elif codigo == 2:
    x_salada = 4.50
    total = x_salada * quantidade
    print('Total: R$ {:.2f}'.format(total))
if codigo == 3:
    x_bacon = 5.0
    total = x_bacon * quantidade
    print('Total: R$ {:.2f}'.format(total))
elif codigo == 4:
    torrada_simples = 2.0
    total = torrada_simples * quantidade
    print('Total: R$ {:.2f}'.format(total))
if codigo == 5:
    refrigerente = 1.50
    total = refrigerente * quantidade
    print('Total: R$ {:.2f}'.format(total))


