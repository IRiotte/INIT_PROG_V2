import API_matriceN as matrice_util

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

def colle_sousèmatrice(matrice, sous_matrice, ligne_haut, colonne_gauche):



    ...

