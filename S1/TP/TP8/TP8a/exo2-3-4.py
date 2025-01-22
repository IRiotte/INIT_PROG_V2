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
    """Fonction qui vérifie si au moins 3 chiffre sont présents dans le mot de passe

    Args:
        mot_de_passe (str): le mot de passe à vérifier

    Returns:
        bool: True si  au moins 3 chiffre est présent, False sinon

    Invariants: aucun chiffre n'est présent dans les caractères déjàà parcourus.
    """    
    nbr_chiffre = 0
    ind = 0
    while ind < len(mot_de_passe) and nbr_chiffre < 4:
        if mot_de_passe[ind] in "0123456789":
            nbr_chiffre += 1
        ind += 1
    return nbr_chiffre >= 3

def chiffre_consecutif_present(mot_de_passe):
    """Fonction qui vérifie si deux chiffres sont consécutif dans un mot de passe.

    Args:
        mot_de_passe (str): le mot de passe à vérifier

    Returns:
        bool: True si deux chiffres sont consécutif dans le mot de passe, False sinon.

    Invariants: aucun chiffre n'est présent dans les caractères déjà parcourus.
    """    
    consecutif = False
    ind = 0
    while ind < len(mot_de_passe) - 1 and not consecutif:
        if mot_de_passe[ind] in "0123456789":
            if mot_de_passe[ind+1] in "0123456789":
                consecutif = True
        ind += 1
    return consecutif

def plus_petit_une_fois(mot_de_passe):
    """Fonction qui vérifie si le plus petit chiffre du mot de passe est présent qu'une
    seule fois.

    Args:
        mot_de_passe (str): le mot de passe à vérifier

    Returns:
        bool: True si le plus petit chiffre du mot de passe est présent une seule
        fois, False sinon.

    Invariants: aucun chiffre n'est présent dans les caractères déjà parcourus.
    """    
    mini = None
    nbr_occurence = 0
    for carac in mot_de_passe:
        if carac in "0123456789":
            if mini is None or mini > carac:
                mini = carac
                nbr_occurence = 1
            elif carac == mini:
                nbr_occurence += 1
    return nbr_occurence == 1


#exo3

import csv

def dialogue_mot_de_passe():
    login = input("Entrez votre nom : ")
    mot_de_passe_correct = False
    while not mot_de_passe_correct :
        mot_de_passe = input("Entrez votre mot de passe : ")
        # Je gère l'affichage
        if not longueur_ok(mot_de_passe):
            print("Votre mot de passe doit comporter au moins 8 caractères")
        elif not chiffre_ok(mot_de_passe):
            print("Votre mot de passe doit comporter au moins 3 un chiffre")
        elif not sans_espace(mot_de_passe):
            print("Votre mot de passe ne doit pas comporter d'espace")
        elif not plus_petit_une_fois(mot_de_passe):
            print("Votre mot de passe ne doit comporter qu'une seule fois le plus petit chiffre.")		 
        elif chiffre_consecutif_present(mot_de_passe):
            print("Votre mot de passe ne doit pas comporter deux chiffres consécutifs")	  
        else:
            mot_de_passe_correct = True        
            print("Votre mot de passe est correct")
            list_mdp = []
            with open("./mdpUltraSecret.txt", 'r') as fichier:
                reader = csv.reader(fichier)
                for ligne in reader:
                    list_mdp.append(ligne)
            print(list_mdp)
            if not ([login + " : " + mot_de_passe] in list_mdp):
                with open("./mdpUltraSecret.txt", 'a') as fichier:
                    writer = csv.writer(fichier)
                    ligne = [login + " : " + mot_de_passe]
                    writer.writerow(ligne)
    return mot_de_passe

dialogue_mot_de_passe()