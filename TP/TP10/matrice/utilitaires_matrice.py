""" Fonctions utilitaires pour manipuler les matrices """

import API_matrice2 as matrice_util


def get_ligne(matrice, ligne):
    """Fonction qui renvoie la liste des éléments d'une ligne donnée d'une matrice

    Args:
        matrice : une matrice quelconque
        ligne (int): le numéro de la ligne (commence à 0)

    Returns:
        list: la liste des éléments de la liste.

    Complexité : O(N)
    """
    liste_ligne = []
    nb_colonne = matrice_util.get_nb_colonnes(matrice)
    for i in range(nb_colonne):
        liste_ligne.append(matrice_util.get_val(matrice, ligne, i))
    return liste_ligne

def get_colonne(matrice, colonne):
    """Fonlction qui renvoie la liste des éléments d'une colonne donnée d'une matrice

    Args:
        matrice : une matrice quelconque
        colonne (int): le numéro de la colonne (commence à 0)

    Returns:
        liste: la liste des éléments de la colonne

    Complexité : O(N)
    """
    liste_col = []
    nb_ligne = matrice_util.get_nb_lignes(matrice)
    for i in range(nb_ligne):
        liste_col.append(matrice_util.get_val(matrice, i, colonne))
    return liste_col

def get_diagonale_principale(matrice):
    """Fonction qui renvoie la liste des éléments de la diagonale principale d'une
    matrice (en haut à gauche à en bas à droite)

    Args:
        matrice : une matrice quelconque

    Returns:
        liste:  la liste des éléments de a diagonale

    Complexité : O(N)
    """
    liste_diag = []
    nb_col = matrice_util.get_nb_colonnes(matrice)
    for i in range(nb_col):
        liste_diag.append(matrice_util.get_val(matrice, i, i))
    return liste_diag

def get_diagonale_secondaire(matrice):
    """Fonction qui renvoie la liste des éléments de la diagonale principale d'une
    matrice (en haut à droite à en bas à gauche)

    Args:
        matrice : une matrice quelconque

    Returns:
        liste:  la liste des éléments de a diagonale

    Complexité : O(N)
    """
    liste_diag = []
    nb_col = matrice_util.get_nb_colonnes(matrice)
    for i in range(nb_col):
        liste_diag.append(matrice_util.get_val(matrice, i, nb_col - i-1))
    return liste_diag

def transpose(matrice):
    """Fonction qui renvoie la matrice transposée d'une matrice donnée

    Args:
        matrice: une matrice quelconque

    Returns:
        (matrice): la transposée de la matrice

    Complexité : O(N^2)
    """
    nb_col = matrice_util.get_nb_colonnes(matrice)
    nb_ligne = matrice_util.get_nb_lignes(matrice)
    mat_transp = matrice_util.matrice(nb_col, nb_ligne, None)
    for i in range(nb_col):
        for j in range(nb_ligne):
            val = matrice_util.get_val(matrice, j, i)
            matrice_util.set_val(mat_transp, i, j, val)
    return mat_transp

def is_triangulaire_inf(matrice):
    """Fonction qui renvoie si une matrice est une matrice triangulaire inférieure

    Args:
        matrice : une matrice quelconque

    Returns:
        bool: True si la matrice est triangulaire inférieure, False sinon

    Complexité : O(N^2)
    """
    nb_col = matrice_util.get_nb_colonnes(matrice)
    nb_ligne = matrice_util.get_nb_lignes(matrice)
    for i in range(nb_ligne):
        for j in range(i+1, nb_col):
            val = matrice_util.get_val(matrice, i, j)
            if val != 0:
                return False
    return True

def is_triangulaire_sup(matrice):
    """Fonction qui renvoie si une matrice est une matrice triangulaire supérieure

    Args:
        matrice : une matrice quelconque

    Returns:
        bool: True si la matrice est triangulaire supérieure, False sinon

    Complexité : O(N^2)
    """
    nb_col = matrice_util.get_nb_colonnes(matrice)
    nb_ligne = matrice_util.get_nb_lignes(matrice)
    for j in range(nb_col):
        for i in range(i+1, nb_ligne):
            val = matrice_util.get_val(matrice, i, j)
            if val != 0:
                return False
    return True

def bloc(matrice, ligne, colonne, hauteur, largeur):
    """Fonction qui renvoie la matrice de taille donnée (inférieure à la matrice d'origine),
     commençant à un indice donné d'une matrice

    Args:
        matrice: _description_
        ligne (int): l'indice de la ligne de départ (commence à 0)
        colonne (int): l'indice de la colonne de départ (commence à 0)
        hauteur (int): le nombre de lignes du bloc
        largeur (int): le nombre de colonnes du bloc

    Returns:
        (matrice): le bloc final

    Complexité : O(N^2)
    """    
    mat_bloc = matrice_util.matrice(hauteur, largeur, None)
    for i in range(hauteur):
        for j in range(largeur):
            nouv_val = matrice_util.get_val(matrice, ligne+i, colonne+j)
            matrice_util.set_val(mat_bloc, i, j, nouv_val)
    return mat_bloc

def somme(matrice1, matrice2):
    """Fonction qui renvoie la matrice résultant de la somme de deux matrices

    Args:
        matrice1 (matrice): une matrice quelconque
        matrice2 (matrice): une matrice quelconque
    """
    nb_col1 = matrice_util.get_nb_colonnes(matrice1)
    nb_col2 = matrice_util.get_nb_colonnes(matrice2)
    nb_ligne1 = matrice_util.get_nb_lignes(matrice1)
    nb_ligne2 = matrice_util.get_nb_lignes(matrice2)
    if nb_ligne1 == nb_ligne2 and nb_col1 == nb_col1:
        matrice_som = matrice_util.matrice(nb_ligne1, nb_col1, None)
    for i in range(nb_ligne1):
        for j in range(nb_col1):
            val1 = matrice_util.get_val(matrice1, i, j)
            val2 = matrice_util.get_val(matrice1, i, j)
            matrice_util.set_val(matrice_som, i, j, val1+val2)
    return matrice_som

#def produit(mat1, mat2)
#
#   ...