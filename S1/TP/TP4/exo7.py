def n_bool(n_ind):
    """Fonction qui renvoie une liste de n+1 True sauf
    les deux premiers élements qui sont des False

    Args:
        n_ind (int): la longueur de la liste créée - 1

    Returns:
        list: la liste des booléens
    """
    return [False, False] + [True for i in range(n_ind-1)]

print(n_bool(5))

def multiple_x(liste_bool, val_x):
    """Fonction qui modifie une liste de booléens et qui mais 
    à False tous les multiple d'un entier x sauf lui-même

    Args:
        liste_bool (list): liste de booléens
        val_x (int): un entier positif
    """    
    for i in range(len(liste_bool)):
        if i != val_x and i % val_x == 0:
            liste_bool[i] = False

#liste_test = n_bool(6)
#multiple_x(liste_test, 2)
#print(liste_test)

def crible_erath(n_entier):
    """Fonction qui applique le crible d'érathosthène sur les n+1 premiers entiers naturels,
    et qui renvoie la liste des nombre premiers parmis eux.

    Args:
        n_entier (int): un entier positif

    Returns:
        list: une liste contenant les nombres premiers parmis les n+1 premiers entiers naturels
    """    
    liste_bool =  n_bool(n_entier)
    liste_nbr_premier = []
    for i in range(2,n_entier+1):
        if liste_bool[i]:
            liste_nbr_premier.append(i)
            multiple_x(liste_bool,i)
    return liste_nbr_premier


def test_crible():
    assert crible_erath(0) == []
    assert crible_erath(1) == []
    assert crible_erath(6) == [2,3,5]
    assert crible_erath(13) == [2,3,5,7,11,13]
    assert crible_erath(2) == [2]

#print(crible_erath(6))