Joueur1 = input('Entrez le nom du Joueur1:').capitalize()
PvJoueur1 = int(input('Entrez le nombre de pv du Joueur1:'))

Joueur2 = input('Entrez le nom du Joueur2:').capitalize()
PvJoueur2 = int(input('Entrez le nombre de pv du Joueur2:'))

print()

message = Joueur1 + '(' + str(PvJoueur1) + 'PV) affronte ' + Joueur2 + '(' + str(PvJoueur2) + 'PV)'
print('+' * (len(message)+4))
print('+',message, '+')
print('+'*(len(message)+4))

print()
