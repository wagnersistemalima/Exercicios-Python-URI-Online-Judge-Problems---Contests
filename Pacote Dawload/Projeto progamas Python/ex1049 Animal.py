#ex1049 Animal
classe1 = str(input())
classe2 = str(input())
classe3 = str(input())
if classe1 == 'vertebrado' :
    if classe2 == 'ave' :
        if classe3 == 'carnivoro' :
            print('aguia')
        elif classe3 == 'onivoro' :
            print('pomba')
    elif classe2 == 'mamifero' :
        if classe3 == 'onivoro' :
            print('homem')
        elif classe3 == 'herbivoro' :
            print('vaca')
elif classe1 == 'invertebrado' :
    if classe2 == 'inseto':
        if classe3 == 'hematofago' :
            print('pulga')
        elif classe3 == 'herbivoro' :
            print('lagarta')
    elif classe2 == 'anelideo' :
        if classe3 == 'hematofago' :
            print('sanguessuga')
        elif classe3 == 'onivoro' :
            print('minhoca')


