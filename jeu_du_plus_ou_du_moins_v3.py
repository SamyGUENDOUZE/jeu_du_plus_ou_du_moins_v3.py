from random import *
rep='oui'
while (rep=='oui'):

    n = randint(0, 1000)

    print(f"Vous devez deviner un nombre entre 0 et 1000.")
    essai = 0                      # Compteur de coups

    while True:                     # Boucle infinie: sortie explicite par break
        try:
            u = int(input("Choisir un nombre entre 0 inclus et 1000 inclus: "))      
            if not 0 < u < 1001:
                raise ValueError()

        except ValueError:       # Sert à gérer le programme si l'utilisateur se trompe dans sa saisie
            print(f"Il faut taper pas un nombre entier compris entre 0 et 1000.")
            continue                # Nouvel essai

        except (KeyboardInterrupt, EOFError):  # Sert à gérer si l'utilsateur quitte le programme
            print("\nVous abandonnez après seulement "
                f"{essai} coup{'s' if essai > 1 else ''}!")
            break                   # Interrompt la boucle while

        # Si la proposition est valide, le jeu peut continuer.
        essai += 1
        if n > u:
            print("C'est plus")
        elif n < u :
            print("C'est moins")
        else:
            print(f"Bravo, Vous avez trouvé en {essai} coup{'s' if essai > 1 else ''}!")
            break                   
    
    rep=input("Voulez-vous continuer(oui/non) : ")
print('Salut, à la prochaine:)')
