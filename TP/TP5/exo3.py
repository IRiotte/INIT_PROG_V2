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
    assert seuil_som_elem([5,7,9,4,5], 5)
    assert not seuil_som_elem([5,7,9,4,5], 1100)
    assert not seuil_som_elem([], 5)
    assert not seuil_som_elem([5], 5)
    assert not seuil_som_elem([5], 9)
    assert seuil_som_elem([8], 2)
    assert not seuil_som_elem([5,2,3,4,1], 15)


def  est_adresse_mail(chaine):
    """Fonction qui vérifie qu'une chaîne de caractères correspond
    à une adresse e-mail potentielle.

    Args:
        chaine (str): une chaîne de caractères

    Returns:
        bool: True si la chaîne est une adresse e-mail potentielle,
        False sinon
    
    Invariant: 
        nb_arob contient le nombre d'occurences de @ dans les caractères
    déjà parcourus.
        ch_apres_arob contient les caractères présents apres le premier @ de la
    chaîne parmis les caractères déjà parcourus s'il y en à un
    """
    nb_arob = 0
    ch_apres_arob = ""
    if len(chaine) > 3: #le mail possède au moins 4 caractères
        if chaine[0] != "@" and chaine[-1] != ".":
            for carac in chaine:
                if carac == "@":
                    nb_arob += 1
                if nb_arob > 0:
                    ch_apres_arob += carac
            if "." in ch_apres_arob:
                if not " " in chaine:
                    if nb_arob == 1:
                        return True
    return False

def test_email():
    assert est_adresse_mail("jean@gmail.com")
    assert est_adresse_mail("jean.zezf@gmail.com")
    assert est_adresse_mail("jean.htt@gm.ail.com")
    assert not est_adresse_mail("jea@n@gmail.com")
    assert not est_adresse_mail("@jean@gmail.com")
    assert not est_adresse_mail("jean@qsdaz..")
    assert not est_adresse_mail("jean@qsdaz.@")
    assert not est_adresse_mail("je suis@je.an")
    assert est_adresse_mail("j@.e")
    assert not est_adresse_mail("")