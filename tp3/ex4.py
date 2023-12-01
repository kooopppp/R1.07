n = 0
n=int(input("veuillez entrez un nombre réel :"))
if n < 0:
    print("retentez")

print("(1): boucle while")
print("(2): boucle for")
x= int(input("choisir entre 1 et 2 "))

if x == 1 :
    y = 1
    while n > 1:
        y *= n

        y -= 1
    print(y)









