#ex1040  Média 3 10/04/2020
nota1, nota2, nota3, nota4 = map(float, input().split())
peso1 = 2
peso2 = 3
peso3 = 4
peso4 = 1
soma_peso = peso1 + peso2 + peso3 + peso4
media = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3 + nota4 * peso4) / soma_peso
if media >= 7.0:
    print('Media: {:.1f}'.format(media))
    print('Aluno aprovado.')
elif media < 5.0:
    print('Media: {:.1f}'.format(media))
    print('Aluno reprovado.')
if media >= 5.0 and media <= 6.9:
    print('Media: {:.1f}'.format(media))
    print('Aluno em exame.')
    exame = float(input())
    print('Nota do exame: {:.1f}'.format(exame))
    nova_media = (exame + media) / 2
    if nova_media >= 5.0:
        print('Aluno aprovado.\nMedia final: {:.1f}'.format(nova_media))




