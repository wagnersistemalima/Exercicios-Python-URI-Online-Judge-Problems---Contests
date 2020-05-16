#Ex1114 Senha Fixa
validacao = int(input())
senha = 2002
while validacao != senha:
    print('Senha Invalida')
    validacao = int(input())
    if validacao == senha:
        print('Acesso Permitido')



