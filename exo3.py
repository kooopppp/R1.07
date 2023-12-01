from random import randrange
y= randrange(0,100)

def nombre(x):
    n = -1
    while n != x:
        n = int(input("entrez un nombre :"))
        if n > x:
            print("le nombre est plus petit")
        if n < x :
            print("le nombre est plus grand")
    print("vous avez trouvé, bien joué!")

nombre(y)