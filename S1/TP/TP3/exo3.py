# exercice 3
def nb_mots(phrase):
    """Fonction qui compte le nombre de mots d'une phrase

    Args:
        phrase (str): une phrase dont les mots sont
        séparés par des espaces (éventuellement plusieurs)

    Returns:
        int: le nombre de mots de la phrase
    """    
    resultat = 0
    prec = ' '
    # au début de chaque tour de boucle
    # prec vaut
    # courant vaut
    # resultat vaut
    for courant in phrase:
        if prec == ' ' and courant != ' ':
            resultat = resultat + 1
        prec = courant
    return resultat+1


def test_nb_mots():
    assert nb_mots("bonjour, il fait beau") == 4
    assert nb_mots("houla!     je    mets beaucoup   d'  espaces    ") == 6
    assert nb_mots(" ce  test ne  marche pas ") == 5
    assert nb_mots("") == 0  # celui ci non plus


nb_mots("bonjour, il fait beau")
nb_mots("houla!     je    mets beaucoup   d'  espaces    ")
nb_mots(" ce  test ne  marche pas ")
nb_mots("")

