minutes= int(input("tapez le nombre de minutes : "))
minute = minutes//60//24//31
print(minute, "minutes restantes")
jour= minutes//60//24
print(jour, 'jours')

mois= jour//31
print(mois, 'mois')
