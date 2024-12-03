""" Matrices : API n 1 """

import csv

def matrice(nb_lignes, nb_colonnes, valeur_par_defaut):
    """crée une nouvelle matrice en mettant la valeur par défaut dans chacune de ses cases.

    Args:
        nb_lignes (int): le nombre de lignes de la matrice
        nb_colonnes (int): le nombre de colonnes de la matrice
        valeur_par_defaut : La valeur que prendra chacun des éléments de la matrice

    Returns:
        une nouvelle matrice qui contient la valeur par défaut dans chacune de ses cases
    """
    return (nb_lignes, nb_colonnes, [valeur_par_defaut for i in range(nb_colonnes*nb_lignes)])



def set_val(la_matrice, ligne, colonne, nouvelle_valeur):
    """permet de modifier la valeur de l'élément qui se trouve à la ligne et à la colonne
    spécifiées. Cet élément prend alors la valeur nouvelle_valeur

    Args:
        la_matrice : une matrice
        ligne (int) : le numéro d'une ligne (la numérotation commence à zéro)
        colonne (int) : le numéro d'une colonne (la numérotation commence à zéro)
        nouvelle_valeur : la nouvelle valeur que l'on veut mettre dans la case

    Returns:
        None
    """
    try:
        la_matrice[2][ligne*la_matrice[1] + colonne] = nouvelle_valeur
    except:
        return None

def get_nb_lignes(la_matrice):
    """permet de connaître le nombre de lignes d'une matrice

    Args:
        la_matrice : une matrice

    Returns:
        int : le nombre de lignes de la matrice
    """
    return la_matrice[0]


def get_nb_colonnes(la_matrice):
    """permet de connaître le nombre de colonnes d'une matrice

    Args:
        la_matrice : une matrice

    Returns:
        int : le nombre de colonnes de la matrice
    """
    try:
        return la_matrice[1]
    except:
        return None


def get_val(la_matrice, ligne, colonne):
    """permet de connaître la valeur de l'élément de la matrice dont on connaît
    le numéro de ligne et le numéro de colonne.

    Args:
        la_matrice : une matrice
        ligne (int) : le numéro d'une ligne (la numérotation commence à zéro)
        colonne (int) : le numéro d'une colonne (la numérotation commence à zéro)

    Returns:
        la valeur qui est dans la case située à la ligne et la colonne spécifiées
    """
    try: 
        mat_col = get_nb_colonnes(la_matrice)
        return la_matrice[2][ligne*mat_col + colonne]
    except:
        return None

# Fonctions pour l'affichage

def affiche_ligne_separatrice(la_matrice, taille_cellule=4):
    """fonction auxilliaire qui permet d'afficher (dans le terminal)
    une ligne séparatrice

    Args:
        la_matrice : une matrice
        taille_cellule (int, optional): la taille d'une cellule. Defaults to 4.
    """
    print()
    for _ in range(get_nb_colonnes(la_matrice) + 1):
        print('-'*taille_cellule+'+', end='')
    print()


def affiche(la_matrice, taille_cellule=4):
    """permet d'afficher une matrice dans le terminal

    Args:
        la_matrice : une matrice
        taille_cellule (int, optional): la taille d'une cellule. Defaults to 4.
    """
    nb_colonnes = get_nb_colonnes(la_matrice)
    nb_lignes = get_nb_lignes(la_matrice)
    print(' '*taille_cellule+'|', end='')
    for i in range(nb_colonnes):
        print(str(i).center(taille_cellule) + '|', end='')
    affiche_ligne_separatrice(la_matrice, taille_cellule)
    for i in range(nb_lignes):
        print(str(i).rjust(taille_cellule) + '|', end='')
        for j in range(nb_colonnes):
            print(str(get_val(la_matrice, i, j)).rjust(taille_cellule) + '|', end='')
        affiche_ligne_separatrice(la_matrice, taille_cellule)
    print()


# Ajouter ici les fonctions supplémentaires, sans oublier de compléter le fichier
# tests_API_matrice.py avec des fonctions de tests

def charge_matrice_str(nom_fichier):
    """permet créer une matrice de str à partir d'un fichier CSV.

    Args:
        nom_fichier (str): le nom d'un fichier CSV (séparateur  ',')

    Returns:
        une matrice de str
    """
    matrice = []
    nb_ligne = 0
    nb_colonne = 0
    with open(nom_fichier) as matrice_csv:
        matrice_reader = csv.reader(matrice_csv, delimiter=",")
        for ligne in matrice_reader:
            ligne.remove("")
            matrice += ligne
            nb_ligne += 1
        nb_colonne = len(ligne)
    return (nb_ligne, nb_colonne, matrice)


def sauve_matrice(la_matrice, nom_fichier):
    """permet sauvegarder une matrice dans un fichier CSV.
    Attention, avec cette fonction, on perd l'information sur le type des éléments

    Args:
        matrice : une matrice
        nom_fichier (str): le nom du fichier CSV que l'on veut créer (écraser)

    Returns:
        None
    """
    with open(nom_fichier) as matrice_csv:
        matrice_writer = csv.writer(matrice_csv, delimiter=",")
        ligne = []
        cpt = 0
        for elem in la_matrice[2]:
            ligne.append(elem)
            cpt += 1
            if cpt == la_matrice[2]:
                matrice_writer.writerow(ligne)


def get_ligne(matrice, ligne):

    liste_ligne = []
    longueur_colonne = get_nb_colonnes(matrice)
    for i in range(longueur_colonne*ligne, longueur_colonne*(ligne+1)):
        liste_ligne.append(matrice[2][i])
    return liste_ligne

def get_colonne(matrice, colonne):

    liste_col = []
    nb_col = get_nb_colonnes(matrice)
    nb_ligne = get_nb_lignes(matrice)
    for i in range(0+colonne, nb_col*nb_ligne, nb_col):
        liste_col.append(matrice[2][i])
    return liste_col

def get_diagonale_principale(matrice):

    ...

def get_diagonale_secondaire(matrice):

    ...

def transpose(matrice):

    ...

def is_triangulaire_inf(matrice):

    ...

def bloc(matrice, ligne, colonne, hauteur, largeur):
    
    ...