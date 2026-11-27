def saisir_nombre(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Erreur : entrez un nombre valide.")


def saisir_operateur():
    while True:
        op = input("Choisissez (+, -, *, /) : ")

        if op in ["+", "-", "*", "/"]:
            return op

        print("Erreur : opérateur invalide.")
