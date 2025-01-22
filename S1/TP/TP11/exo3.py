import API_matrice2 as matrice_util

def sous_matrice(matrice, hauteur, largeur, ligne, colonne):
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

def colle_sous_matrice(matrice, sous_matrice, ligne_haut, colonne_gauche):
    """Fonction qui colle une sous matrice dans une matrice à partir
    de la position supérieure gauche d'indices donnés.

    Args:
        matrice : une matrice quelconque
        sous_matrice : une matrice quelconque
        ligne_haut (int): l'indice de la ligne du coin supérieur gauche du collage
        colonne_gauche (int): _description_
    """
    nb_ligne_sm = matrice_util.get_nb_lignes(sous_matrice)
    nb_col_sm = matrice_util.get_nb_colonnes(sous_matrice)
    nb_ligne_m = matrice_util.get_nb_lignes(matrice)
    nb_col_m = matrice_util.get_nb_colonnes(matrice)

    if nb_ligne_sm + ligne_haut <= nb_ligne_m and nb_col_sm + colonne_gauche <= nb_col_m:
        for i in range(nb_ligne_sm):
            for j in range(nb_col_sm):
                nouv_val = matrice_util.get_val(sous_matrice, i, j)
                matrice_util.set_val(matrice, i+ligne_haut, j+colonne_gauche, nouv_val)
    else:
        print("erreur lors du collage")



