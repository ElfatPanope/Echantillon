Joueur1 = input('Entrez le nom du Joueur1:').capitalize()
Pv1 = int(input('Entrez le nombre de pv du Joueur1:'))

Joueur2 = input('Entrez le nom du Joueur2:').capitalize()
Pv2 = int(input('Entrez le nombre de pv du Joueur2:'))

print()

message = Joueur1 + '(' + str(Pv1) + 'PV) affronte ' + Joueur2 + '(' + str(Pv2) + 'PV)'
print('+' * (len(message)+4))
print('+',message, '+')
print('+'*(len(message)+4))

print()

att1 =int(input(Joueur1+',combien de dégats infligez-vous à '+ Joueur2 + '?'))
print()
Pv2 -= att1
msg1 = Joueur1+ ' attaque '+Joueur2+' et lui inflige '+str(att1)+' PV'
msg2 = Joueur2+' a maintenant '+str(Pv2)+' PV'
max_size = max(len(msg1), len(msg2))
msg1 += ' ' * (max_size - len(msg1))
msg2 += ' ' * (max_size-len(msg2))
print('+'* (max_size+4))
print('+', msg1,'+')
print('+', msg2, '+')
print('+'*(max_size + 4))

print()

att2 =int(input(Joueur2+',combien de dégats infligez-vous à '+ Joueur1 + '?'))
print()
Pv1 -= att2
msg1 = Joueur2 + ' attaque ' + Joueur1 +' et lui inflige '+ str(att2) +' PV '
msg2 = Joueur1 + ' a maintenant ' + str(Pv1) +' PV '
max_size = max(len(msg1), len(msg2))
msg1 += ' ' * (max_size - len(msg1))
msg2 += ' ' * (max_size-len(msg2))
print('+'* (max_size+4))
print('+', msg1,'+')
print('+', msg2, '+')
print('+'*(max_size + 4))

print()

msg1 = ' Résultat du combat : '
msg2 = Joueur1 +' a '+ str(Pv1)+' PV'
msg3 = Joueur2 +' a '+ str(Pv2)+' PV'
max_size = max(len(msg1), len(msg2), len(msg3))
msg1 += ' ' * (max_size - len(msg1))
msg2 += ' ' * (max_size-len(msg2))
msg3 += ' ' * (max_size - len(msg3))
print('+'* (max_size+4))
print('+', msg1,'+')
print('+', msg2, '+')
print('+', msg3, '+')
print('+'*(max_size + 4))