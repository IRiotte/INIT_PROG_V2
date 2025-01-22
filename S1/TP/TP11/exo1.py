# liste de tuples (nom, prix)
import API_matrice2 as matrice_util

def affiche_bilan_financier(week_end):

    dict_somme = {}
    somme_total = 0
    for (prenom, prix) in week_end:
        dict_somme[prenom] = dict_somme.get(prenom, 0) + prix
        somme_total += prix
    # suite de l'exo (la correction a été faite)

def sous_matrice1(matrice, nb_lignes, nb_colonnes, position_haut, position_gauche):
    """renvoie une sous matrice avec comme dimensions nb_lignes et nb_colonnes
    a partir de la position du coin haut-gauche

    Args:
    matrice : _description_
    nb_lignes (int): nombre de lignes de la sous matrice
    nb_colonnes (int): nombres de colonnes de la sous matrice
    position_haut (int): ligne du coin haut-gauche
    position_gauche (int): colonne du coin haut-gauche

    """
    matrice_finale = matrice_util.matrice(nb_lignes,nb_colonnes)
    for i in range(nb_lignes):
        for j in range(nb_colonnes):
            valeur_finale = matrice_util.get_val(matrice,position_haut,position_gauche)
            matrice_finale = matrice_util.set_val(matrice_finale,i,j,valeur_finale)
    return matrice_finale

test = [[1,2,3],
        [4,5,6], 
        [7,8,9]]
print(sous_matrice1(test, 2,2, 1,0))