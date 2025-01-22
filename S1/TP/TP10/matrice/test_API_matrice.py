""" tests pour les API matrices
    Remarques : tous les tests de ce fichier doivent passer
    quelle que soit l'API utilisée
"""
import TP.TP11.API_matrice2 as API
import utilitaires_matrice as uti

def matrice1():
    """ définition d'une matrice pour les tests """
    mat1 = API.matrice(3, 4, None)
    API.set_val(mat1, 0, 0, 10)
    API.set_val(mat1, 0, 1, 11)
    API.set_val(mat1, 0, 2, 12)
    API.set_val(mat1, 0, 3, 13)
    API.set_val(mat1, 1, 0, 14)
    API.set_val(mat1, 1, 1, 15)
    API.set_val(mat1, 1, 2, 16)
    API.set_val(mat1, 1, 3, 17)
    API.set_val(mat1, 2, 0, 18)
    API.set_val(mat1, 2, 1, 19)
    API.set_val(mat1, 2, 2, 20)
    API.set_val(mat1, 2, 3, 21)
    return mat1

def matrice2():
    """ définition d'une matrice pour les tests """
    mat2 = API.matrice(2, 3, None)
    API.set_val(mat2, 0, 0, 'A')
    API.set_val(mat2, 0, 1, 'B')
    API.set_val(mat2, 0, 2, 'C')
    API.set_val(mat2, 1, 0, 'D')
    API.set_val(mat2, 1, 1, 'E')
    API.set_val(mat2, 1, 2, 'F')
    return mat2

def matrice3():
    """ définition d'une matrice pour les tests """
    mat3 = API.matrice(3, 3, None)
    API.set_val(mat3, 0, 0, 2)
    API.set_val(mat3, 0, 1, 7)
    API.set_val(mat3, 0, 2, 6)
    API.set_val(mat3, 1, 0, 9)
    API.set_val(mat3, 1, 1, 5)
    API.set_val(mat3, 1, 2, 1)
    API.set_val(mat3, 2, 0, 4)
    API.set_val(mat3, 2, 1, 3)
    API.set_val(mat3, 2, 2, 8)
    return mat3

def test_get_nb_lignes():
    """ tests get_nb_lignes """
    matrice_1 = matrice1()
    matrice_2 = matrice2()
    matrice_3 = matrice3()
    assert API.get_nb_lignes(matrice_1) == 3
    assert API.get_nb_lignes(matrice_2) == 2
    assert API.get_nb_lignes(matrice_3) == 3

def test_get_nb_colonnes():
    """ tests pour get_nb_colonnes """
    mat_1 = matrice1()
    mat_2 = matrice2()
    mat_3 = matrice3()
    assert API.get_nb_colonnes(mat_1) == 4
    assert API.get_nb_colonnes(mat_2) == 3
    assert API.get_nb_colonnes(mat_3) == 3

def test_get_val():
    """ tests pour get_val """
    matr1 = matrice1()
    matr2 = matrice2()
    matr3 = matrice3()
    assert API.get_val(matr1, 0, 1) == 11
    assert API.get_val(matr1, 2, 1) == 19
    assert API.get_val(matr2, 1, 1) == 'E'
    assert API.get_val(matr2, 0, 2) == 'C'
    assert API.get_val(matr3, 2, 0) == 4
    assert API.get_val(matr3, 1, 0) == 9

#def test_sauve_charge_matrice():
#    """tests pour sauvegarde et restauration"""
#    la_matrice = matrice2()
#    API.sauve_matrice(la_matrice, "matrice.csv")
#    matrice_bis = API.charge_matrice_str("matrice.csv")
#    assert la_matrice == matrice_bis


#=================================
# 2e partie
#=================================

def test_get_ligne():
    mat1 = matrice1()
    mat2 = matrice2()
    mat3 = matrice3()
    assert uti.get_ligne(mat1, 2) == [18,19,20,21]
    assert uti.get_ligne(mat2, 1) == ["D", "E", "F"]
    assert uti.get_ligne(mat3, 0) == [2,7,6]

def test_get_colonne():
    mat1 = matrice1()
    mat2 = matrice2()
    mat3 = matrice3()
    assert uti.get_colonne(mat1, 2) == [12,16,20]
    assert uti.get_colonne(mat2, 1) == ["B", "E"]
    assert uti.get_colonne(mat3, 0) == [2,9,4]

def test_get_diagonale():
    mat3 = matrice3()
    assert uti.get_diagonale_principale(mat3) == [2,5,8]
    assert uti.get_diagonale_secondaire(mat3) == [6,5,4]


def test_transpose():
    mat1 = matrice1()
    mat2 = matrice2()
    mat3 = matrice3()
    transp1 = uti.transpose(mat1)
    transp2 = uti.transpose(mat2)
    transp3 = uti.transpose(mat3)
    assert API.get_nb_colonnes(transp1) == 3
    assert API.get_nb_colonnes(transp2) == 2
    assert API.get_nb_lignes(transp1) == 4
    assert API.get_nb_lignes(transp2) == 3
    assert API.get_val(transp1, 0, 1) == 14
    assert API.get_val(transp1, 2, 1) == 16
    assert API.get_val(transp2, 1, 0) == 'B'
    assert API.get_val(transp2, 0, 1) == 'D'
    assert API.get_val(transp3, 2, 0) == 6
    assert API.get_val(transp3, 1, 0) == 7

def matrice_tri_inf():
    """ définition d'une matrice pour les tests """
    mat3 = API.matrice(3, 3, None)
    API.set_val(mat3, 0, 0, 2)
    API.set_val(mat3, 0, 1, 0)
    API.set_val(mat3, 0, 2, 0)
    API.set_val(mat3, 1, 0, 9)
    API.set_val(mat3, 1, 1, 5)
    API.set_val(mat3, 1, 2, 0)
    API.set_val(mat3, 2, 0, 4)
    API.set_val(mat3, 2, 1, 3)
    API.set_val(mat3, 2, 2, 8)
    return mat3

def test_is_triangulaire_inf():
    mat3 = matrice3()
    mat_tri = matrice_tri_inf()
    assert not uti.is_triangulaire_inf(mat3)
    assert uti.is_triangulaire_inf(mat_tri)
    
def test_bloc():
    mat1 = matrice1()
    mat2 = matrice2()
    mat3 = matrice3()
    bloc1 = uti.bloc(mat1, 0, 1, 3, 2)
    bloc2 = uti.bloc(mat2, 0, 0, 1, 2)
    bloc3 = uti.bloc(mat3, 1, 1, 2, 2)
    assert API.get_nb_colonnes(bloc1) == 2
    assert API.get_nb_colonnes(bloc2) == 2
    assert API.get_nb_colonnes(bloc3) == 2
    assert API.get_nb_lignes(bloc1) == 3
    assert API.get_nb_lignes(bloc2) == 1
    assert API.get_nb_lignes(bloc3) == 2
    assert API.get_val(bloc1, 0, 1) == 12
    assert API.get_val(bloc1, 2, 1) == 20
    assert API.get_val(bloc2, 0, 0) == 'A'
    assert API.get_val(bloc2, 0, 1) == 'B'
    assert API.get_val(bloc3, 1, 0) == 3
    assert API.get_val(bloc3, 1, 1) == 8

def test_somme():
    mat1 = matrice3()
    mat2 = matrice3()
    mat_som = uti.somme(mat1, mat2)
    assert API.get_val(mat_som, 0, 1) == 14
    assert API.get_val(mat_som, 2, 1) == 6
    assert API.get_val(mat_som, 0, 0) == 4
    assert API.get_val(mat_som, 1, 2) == 2
    assert API.get_val(mat_som, 1, 0) == 18
    assert API.get_val(mat_som, 1, 1) == 10

#def produit():
#
#    ...