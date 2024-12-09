""" Fonctions utilitaires pour manipuler les matrices """

import API_matrice1 as matrice_util


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

    liste_diag = []
    nb_col = get_nb_colonnes(matrice)
    for i in range(nb_col):
        liste_diag.append(matrice[2][nb_col*i + i])
    return liste_diag

def get_diagonale_secondaire(matrice):

    liste_diag = []
    nb_col = get_nb_colonnes(matrice)
    for i in range(1, nb_col+1):
        liste_diag.append(matrice[2][nb_col*i - i])
    return liste_diag

def transpose(matrice):

    liste_transp = []
    nb_col = get_nb_colonnes(matrice)
    nb_ligne = get_nb_lignes(matrice)
    for i in range(nb_col):
        for j in range(nb_ligne):
            liste_transp.append(matrice[2][nb_col*j + i])
    return liste_transp

def is_triangulaire_inf(matrice):

    ...

def bloc(matrice, ligne, colonne, hauteur, largeur):
    
    ...