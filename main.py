from operations import *
from validation import *

while True:
    print("\n=== MINI CALCULATRICE ===")
    print("1. Calculer")
    print("2. Quitter")

    choix = input("Votre choix : ")

    if choix == "2":
        print("Au revoir !")
        break

    elif choix == "1":
        a = saisir_nombre("Premier nombre : ")
        op = saisir_operateur()
        b = saisir_nombre("Deuxième nombre : ")

        try:
            if op == "+":
                resultat = addition(a, b)
            elif op == "-":
                resultat = soustraction(a, b)
            elif op == "*":
                resultat = multiplication(a, b)
            else:
                resultat = division(a, b)

            print("Résultat :", resultat)

        except ZeroDivisionError as e:
            print("Erreur :", e)

    else:
        print("Choix invalide.")
