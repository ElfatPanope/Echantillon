# Demander à l'utilisateur d'entrer les nombres et l'opération
nombre_a_gauche = input("Entrez le premier nombre : ")
nombre_a_droite = input("Entrez le deuxième nombre : ")
operation = input("Entrez l'opération (+, -, *, /) : ")

# Vérifier si les nombres sont des entiers
if nombre_a_gauche.isnumeric() and nombre_a_droite.isnumeric():
    # Convertir les nombres entrés en entiers
    nombre_a_gauche = int(nombre_a_gauche)
    nombre_a_droite = int(nombre_a_droite)

    # Effectuer l'opération en fonction du choix de l'utilisateur
    if operation == "+":
        resultat = nombre_a_gauche + nombre_a_droite
    elif operation == "-":
        resultat = nombre_a_gauche - nombre_a_droite
    elif operation == "*":
        resultat = nombre_a_gauche * nombre_a_droite
    elif operation == "/":
        if nombre_a_droite == 0:
            print("Erreur : Impossible de diviser par zéro.")
        else:
            resultat = nombre_a_gauche / nombre_a_droite
    else:
        print("Erreur : L'opération doit être l'un des symboles suivants : +, -, *, /")
else:
    print("Erreur : Les deux nombres doivent être des entiers.")

if 'resultat' in locals():
    print(f"Le résultat de {nombre_a_gauche} {operation} {nombre_a_droite} est égal à {resultat}")