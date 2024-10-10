def plus_long_plateau(chaine):
    """recherche la longueur du plus grand plateau d'une chaine
    Args:
        chaine (str): une chaine de caractères

    Returns:
        int: la longueur de la plus grande suite de lettres consécutives égales
    """
    lg_max = 1 # longueur du plus grand plateau déjà trouvé
    lg_actuelle = 1  # longueur du plateau actuel
    for i in range(1, len(chaine)):
        if chaine[i] == chaine[i-1]:  # si la lettre actuelle est égale à la précédente
            lg_actuelle += 1
        else:  # si la lettre actuelle est différente de la précédente
            if lg_actuelle > lg_max:
                lg_max = lg_actuelle
            lg_actuelle = 1
    if lg_actuelle > lg_max:  # cas du dernier plateau
        lg_max = lg_actuelle
    if chaine == "":
        lg_max = 0
    return lg_max


def test_long_plat():
    assert plus_long_plateau("pomme") == 2
    assert plus_long_plateau("creee") == 3
    assert plus_long_plateau("aaaat") == 4
    assert plus_long_plateau("aaaaa") == 5
    assert plus_long_plateau("y") == 1
    assert plus_long_plateau("") == 0

