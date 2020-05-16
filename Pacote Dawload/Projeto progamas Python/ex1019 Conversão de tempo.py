#ex1019  Conversão de tempo 09/04/2020
tempo_s = int(input())
hora = tempo_s // 3600
minutos = (tempo_s % 3600) // 60
segundos = (tempo_s % 3600) % 60
print('{}:{}:{}'.format(hora, minutos, segundos))