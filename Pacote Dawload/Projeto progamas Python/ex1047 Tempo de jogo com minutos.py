#1047 Tempo de jogo com minutos 14/04/2020
entrada = input().split()
a, b, c, d = entrada
a = int(a)
b = int(b)
c = int(c)
d = int(d)
inicio = a * 60 + b
fim = c * 60 + d
if inicio < fim:
    hora = (fim - inicio) // 60
    min = (fim - inicio) % 60
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(hora, min))
elif inicio > fim:
    hora = (24 * 60 - inicio + fim) // 60
    min = (24 * 60 - inicio + fim) % 60
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(hora, min))
else:
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')