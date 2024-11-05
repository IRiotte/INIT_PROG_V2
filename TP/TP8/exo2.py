def longueur_ok(mot_de_passe):
    """Fonction qui verifie si la longuueuur du mot de passe n'est
    pas inférieure à 8 caractères.

    Args:
        mot_de_passe (str): le mot de passe à vérifier

    Returns:
        bool: True si la longueuur est bonne, False sinon
    """    
    return len(mot_de_passe) >= 8

def sans_espace(mot_de_passe):
    """Fonction qui vérifie si un mot de passe contient un espace.

    Args:
        mot_de_passe (str): le mot de passe à vérifier

    Returns:
        bool: True si le mot de passe ne contient aucun espace, False sinon
    """    
    return not " " in mot_de_passe

def chiffre_ok(mot_de_passe):
    """Fonction qui vérifie si au moins un chiffre est présent dans le mot de passe

    Args:
        mot_de_passe (str): le mot de passe à vérifier

    Returns:
        bool: True si  au moins un chiffre est présent, False sinon

    Invariants: aucun chiffre n'est présent dans les caractères déjàà parcourus.
    """    
    nbr_chiffre = 0
    ind = 0
    while ind < len(mot_de_passe) and nbr_chiffre < 4:
        if mot_de_passe[ind] in "0123456789":
            nbr_chiffre += 1
        ind += 1
    return nbr_chiffre < 4

def pas_chiffre_consecutif(mot_de_passe):
    """Fonction qui vérifie si au moins un chiffre est présent dans le mot de passe

    Args:
        mot_de_passe (str): le mot de passe à vérifier

    Returns:
        bool: True si  au moins un chiffre est présent, False sinon

    Invariants: aucun chiffre n'est présent dans les caractères déjàà parcourus.
    """    
    consecutif = False
    ind = 0
    while ind < len(mot_de_passe) - 1 and not consecutif:
        if mot_de_passe[ind] in "0123456789":
            if mot_de_passe[ind+1] in "0123456789":
                consecutif = True
        ind += 1
    return consecutif

