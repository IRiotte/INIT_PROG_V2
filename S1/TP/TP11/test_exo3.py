import API_matrice2 as API
import exo3 as uti

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

def test_sous_matrice():
    mat1 = matrice1()
    mat2 = matrice2()
    mat3 = matrice3()
    bloc1 = uti.sous_matrice(mat1, 0, 1, 3, 2)
    bloc2 = uti.sous_matrice(mat2, 0, 0, 1, 2)
    bloc3 = uti.sous_matrice(mat3, 1, 1, 2, 2)
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