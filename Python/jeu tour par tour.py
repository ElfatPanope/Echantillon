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

degatJoueur1 =int(input())
tour1 = Joueur1 + ' , combien infligez-vous de dégats à '+ Joueur2 + ' ? '+ str(degatJoueur1)
print(tour1)
print()
Joueur1attck = Joueur1 + ' attaque ' + Joueur2 + ' qui perd ' + str(degatJoueur1) + ' PV'
print('+'*(len(Joueur1attck)+4))
print('+',Joueur1attck,'+')
pvj2=int(PvJoueur2-degatJoueur1)
vieJoueur2 = Joueur2 + ' a maintenant ' + str(pvj2)+' PV'
print('+',vieJoueur2,'        +')
print('+'*(len(Joueur1attck)+4))
print()
degatJoueur2 =int(input())
tour2 = Joueur2 + ' , combien infligez-vous de dégats à '+ Joueur1 + ' ? '+ str(degatJoueur2)
print(tour2)
print()
Joueur2attck = Joueur2 + ' attaque ' + Joueur1 + ' qui perd ' + str(degatJoueur2) + ' PV'
print('+'*(len(Joueur2attck)+4))
print('+',Joueur2attck,'+')
pvj1=int(PvJoueur1-degatJoueur1)
vieJoueur1 = Joueur1 + ' a maintenant ' + str(pvj1)+' PV'
print('+',vieJoueur1,'           +')
print('+'*(len(Joueur2attck)+4))
print()
resultattour1='Résultat du combat'
print('+'*(len(resultattour1)+4))
print('+',resultattour1,'+')
finPVJ1= Joueur1 + ' a '+ str(pvj1)+' PV'
print('+',finPVJ1,'       +')
finPVJ2= Joueur2 + ' a '+ str(pvj2)+' PV'
print('+',finPVJ2,'    +')
print('+'*(len(resultattour1)+4))