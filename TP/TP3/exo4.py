def somm_nb_pair(liste):
    """Fonction qui renvoie la somme des nombres pairs d'une liste d'entier

    Args:
        liste (list): liste de nombres entiers (int)

    Returns:
        int: la somme des nombres pairs de la liste
    """
    somme = 0
    for entier in liste:
        if entier % 2 == 0:
            somme += entier
    return somme

def test_somm_pair():
    assert somm_nb_pair([4,3,7,9,5]) == 4
    assert somm_nb_pair([1,3,2,9,8]) == 10
    assert somm_nb_pair([1,2,-2,3]) == 0
    assert somm_nb_pair([2]) == 2
    assert somm_nb_pair([]) == 0

test_somm_pair()


def dern_voy_ch_carac(chaine):
    """Fonction qui renvoie la derniere voyelle d'une chaine de caractère

    rgs:
        chaine (str): chaine de caractères
    
    Returns:
        str: la derniere voyelle de la chaine s'il y en a une
    """
    voyelle = None
    for carac in chaine:
        if carac in "aeiouy":
            voyelle = carac
    return voyelle


def test_voy_chaine():
    assert dern_voy_ch_carac("bonjour") == "u"
    assert dern_voy_ch_carac("testi") == "i"
    assert dern_voy_ch_carac("etst") == "e"
    assert dern_voy_ch_carac("aaaaaaa") == "a"
    assert dern_voy_ch_carac("bcdfghjklm") is None
    assert dern_voy_ch_carac("") is None



def prop_nbr_neg(liste):
    """Fonction qui renvoie la proportion de nombres négatifs dans une liste

    Args:
        liste (list): une liste de nombres 'float

    Returns:
        float: la proportion de nombres négatifs de la liste
    """
    quant_nbr_neg = 0
    quant_nbr = 0
    for nbr in liste:
        quant_nbr += 1
        if nbr < 0:
            quant_nbr_neg += 1
    if not quant_nbr == 0:
        proportion = quant_nbr_neg / quant_nbr
    else:
        proportion = 0
    return proportion

def test_prop_neg():
    assert prop_nbr_neg([]) == 0
    assert prop_nbr_neg([1, 2, 3, 4]) == 0
    assert prop_nbr_neg([-1, 2, -7, 4]) == 1/2
    assert prop_nbr_neg([-7,-8,-2,]) == 1
    assert prop_nbr_neg([-1]) == 1
    assert prop_nbr_neg([-1]) == 1
    assert prop_nbr_neg([-1,2,-4]) == 2/3

test_prop_neg()
