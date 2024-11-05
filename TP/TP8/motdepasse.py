# info-pannes.iut45@listes.univ-orleans.fr

# Codé par Papy Force X, jeune padawan de l'informatique

def dialogue_mot_de_passe():
    login = input("Entrez votre nom : ")
    mot_de_passe_correct = False
    while not mot_de_passe_correct :
        mot_de_passe = input("Entrez votre mot de passe : ")
        # Je gère l'affichage
        if not longueur_ok(mot_de_passe):
            print("Votre mot de passe doit comporter au moins 8 caractères")
        elif not chiffre_ok(mot_de_passe):
            print("Votre mot de passe doit comporter au moins un chiffre")
        elif not sans_espace(mot_de_passe):
            print("Votre mot de passe ne doit pas comporter d'espace")	   
        else:
            mot_de_passe_correct = True        
    print("Votre mot de passe est correct")
    return mot_de_passe

#dialogue_mot_de_passe()

def longueur_ok(mot_de_passe):
    """Fonction qui verifie si la longuueuur du mot de passe n'est
    pas inférieure à 8 caractères.

    Args:
        mot_de_passe (str): le mot de passe à vérifier

    Returns:
        bool: True si la longueuur est bonne, False sinon
    """    
    return len(mot_de_passe) >= 8

def chiffre_ok(mot_de_passe):
    """Fonction qui vérifie si au moins un chiffre est présent dans le mot de passe

    Args:
        mot_de_passe (str): le mot de passe à vérifier

    Returns:
        bool: True si  au moins un chiffre est présent, False sinon

    Invariants: aucun chiffre n'est présent dans les caractères déjàà parcourus.
    """    
    for carac in mot_de_passe:
        if carac in "0123456789":
            return True
    return False

def sans_espace(mot_de_passe):
    """Fonction qui vérifie si un mot de passe contient un espace.

    Args:
        mot_de_passe (str): le mot de passe à vérifier

    Returns:
        bool: True si le mot de passe ne contient aucun espace, False sinon
    """    
    return not " " in mot_de_passe

