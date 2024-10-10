def ordre_croissant(liste):
    """Fonction qui renvoie True si une liste est triée dans l'ordre
    croissant, False sinon

    Args:
        liste (list): une liste d'éléments

    Returns:
        bool: True si dans l'ordre croissant, False sinon

    invariant : jusqu'au rang i, la liste est croissante.
    """
    for i in range(len(liste) - 1):
        if liste[i+1] < liste[i]:
            return False
    return True

def test_croissant():
    assert ordre_croissant([0,1,2,3,4,5]) == True
    assert ordre_croissant([0,1,2,3,4,-778]) == False
    assert ordre_croissant([7,1,2,3,4,5]) == False
    assert ordre_croissant([0,1,8,4,3,5]) == False
    assert ordre_croissant([1,1,1,1,1]) == True
    assert ordre_croissant([0]) == True
    assert ordre_croissant([]) == True


def seuil_som_elem(liste, seuil):
    """Fonction qui renvoie vrai si la somme des éléments de la liste
    ne dépasse pas un seuil donné en paramètre.

    Args:
        liste (list): une liste de nombres
        seuil (int): un nombre rprésentant le seuil à ne pas dépasser

    Returns:
        bool: True si la somme à dépassé le seuil, FaLse sinon
    
    invariants:
        somme (int): contient la somme des élémeznts de la liste déjà
        parcourus, sachant que somme <= seuil 
    """
    somme = 0
    for elem in liste:
        somme += elem
        if somme > seuil:
            return True
    return False

def test_seuil():
    assert seuil_som_elem([5,7,9,4,5], 5) == True
    assert seuil_som_elem([5,7,9,4,5], 1100) == False
    assert seuil_som_elem([], 5) == False
    assert seuil_som_elem([5], 5) == False
    assert seuil_som_elem([5], 9) == False
    assert seuil_som_elem([8], 2) == True
    assert seuil_som_elem([5,2,3,4,1], 15) == False


def  est_adresse_mail(chaine):
    """Fonction qui vérifie qu'une chaîne de caractères correspond
    à une adresse e-mail potentielle.

    Args:
        chaine (str): une chaîne de caractères

    Returns:
        bool: True si la chaîne est une adresse e-mail potentielle,
        False sinon
    """                        
    return


