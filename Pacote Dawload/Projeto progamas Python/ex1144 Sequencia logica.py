numero = int(input())
for c in range(1, numero + 1):                      # EX: A sequencia é de 1 a 5, porem ela se repete
    print('{} {} {}'.format(c, c**2, c**3))         # na primeira repetição o contador**2 contador**3
    print('{} {} {}'.format(c, c**2 + 1, c**3 + 1))   # na segunda repetção o contador**2 +1 contador**3 +1