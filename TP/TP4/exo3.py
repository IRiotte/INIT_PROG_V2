def chaine_en_nbr(chaine):
    """Fonction qui renvoie la chaîne de caractères
    en nombre, si elle ne contient que des entiers positifs,
    sinon renvoiee None

    Args:
        chaine (_type_): _description_

    Returns:
        _type_: _description_
    """    
    if not chaine == "":
        nombre = 0
        liste_chiffre = "0123456789"
        for i in range(len(chaine)):
            if chaine[i] in "0123456789":
                nombre = nombre*10 + liste_chiffre.index(chaine[i]) ####
            else:
                return None
    else:
        nombre = None
    return nombre


def test_chain_nbr():
    assert chaine_en_nbr("12") == 12
    assert chaine_en_nbr("12asad") == None
    assert chaine_en_nbr("97854") == 97854
    assert chaine_en_nbr("000") == 0
    assert chaine_en_nbr("111") == 111
    assert chaine_en_nbr("") == None


# A refaire sans le ".index"