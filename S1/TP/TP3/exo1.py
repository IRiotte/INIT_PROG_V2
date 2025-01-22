# exercice 1
def plus_pair_que_impair(liste_nombre):
    """Fonction qui indique si une liste de nombre
    contient plus ou autant de nombres pairs que impairs

    Args:
        liste_nombre (tab): liste de nombre entier (int)

    Returns:
        bool: Vrai si la liste de nombres contient plus ou autant
        de nombres pairs que impairs, Faux sinon
    """
    quant_nbr_pair = 0
    quant_nbr_impair = 0
    # au début de chaque tour de boucle
    #  A COMPLETER
    for nombre in liste_nombre:
        if nombre % 2 == 0:
            quant_nbr_pair += 1
        else:
            quant_nbr_impair += 1
    return quant_nbr_pair >= quant_nbr_impair

def test_mystere():
    assert plus_pair_que_impair([])
    assert not plus_pair_que_impair([1])
    assert plus_pair_que_impair([2, 4, 6, 8])
    assert not plus_pair_que_impair([1, 3, 5, 7])