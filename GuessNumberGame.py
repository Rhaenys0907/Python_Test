import random

nbr=random.randint(1, 100)
guess= False

while not guess :
    try:
        n = int((input("Entrez un nombre entier: ")))
    except Exception :
        print("ERREUR, VEUILLEZ ENTRER UN NOMBRE.")
        continue
    if n==nbr :
        print("BRAVO! C'EST BIEN LE CHIFFRE A DEVINER.")
        guess= True
    elif n>nbr :
        print("Votre chiffre est supérieur au mien, Réessayez!")
    else:
        print("Votre chiffre est inférieur au mien, Réessayez!")



