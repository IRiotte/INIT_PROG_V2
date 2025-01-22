##Exercie 1
def somme_list_nbr(liste):
    """Fonction qui renvoie la somme de chaque
    nombre de la liste 

    Args:
        liste (list): contient des nombres entiers (int)

    Returns:
        int: la somme des nombres de la liste
    """    
    somme = None
    for elem in liste:
        if somme == None:
            somme == elem
        else:
            somme += elem
    return somme

def max_list(liste):
    """Fonction qui renvoie le maximum
    d'une liste de nombres

    Args:
        liste (list): contient des nombres entiers (int)

    Returns:
        int: le maximum de la liste
    """    
    val_max = None
    for elem in liste:
        if val_max == None:
            val_max = elem
        elif elem > val_max:
            val_max = elem
    return val_max

def nbr_occur_lettre(lettre, mot):
    """Fonction qui renvoie le nombre d'occurrence d'une
    lettre dans un mot

    Args:
        lettre (str): la lettre à compter dans le mot
        mot (str): le mot dans lequel compter la lettre

    Returns:
        int: le nombre d'occurrence
    """    
    nbr_occ = 0
    for carac in mot:
        if carac == lettre:
            nbr_occ += 1
    return nbr_occ



##Exercice 2
def min_list(liste):
    """Fonction qui renvoie le minimum de la liste

    Args:
        liste (list): contient des nombres entiers (int)

    Returns:
        int: le minimum de la liste
    """    
    val_min = None
    for elem in liste:
        if val_min == None:
            val_min = elem
        elif elem < val_min:
            val_min = elem
    return val_min

def ecart_plus_petit_plus_grand(liste):
    """fonction qui renvoie l'écart entre le minimum
    et le maximum d'une liste

    Args:
        liste (list): contient des nombres entier (int)

    Returns:
        int: l'écart ent le max et le min
    """    
    v_min = None
    v_max = None
    for elem in liste:
        if v_min == None:
            v_min = elem
            v_max = elem
        elif elem < v_min:
            v_min = elem
        elif elem > v_max:
            v_max = elem
    ecart = v_max - v_min
    return ecart

def nbr_elem_sup_10(liste):
    """Fonction qui renvoie le nombre d'éléments de la liste
    qui sont supérieurs à 10

    Args:
        liste (list): contient des nombres entiers (int)

    Returns:
        int: le nombred d'élément supérieurs à 10
    """    
    nbr_sup_10 = 0
    for elem in liste:
        if elem > 10:
            nbr_sup_10 += 1
    return nbr_sup_10

def nbr_elem_neg(liste):
    """Fonction qui renvoie le nombre d'éléments négatifs
    d'une liste

    Args:
        liste (list): contient des nombres entiers (int)

    Returns:
        int: le nombre de négatifs
    """    
    elem_neg = 0
    for elem in liste:
        if elem < 0:
            elem_neg += 1
    return elem_neg

def moyenne_nbr_neg(liste):
    """Fonction qui renvoie la moyenne de nombres négatifs
    parmi tous les nombres d'une liste

    Args:
        liste (list): contient des nombres entiers (int)

    Returns:
        float: la moyenne des négatifs
    """    
    moyenne = None
    nbr_neg = 0
    nbr_elem = 0
    for elem in liste:
        nbr_elem += 1
        if elem < 0:
            nbr_neg += 1
    if not nbr_elem == 0:
        moyenne = nbr_neg / nbr_elem
    return moyenne



##Exercice 3
def est_ce_nouv_syll(syll, lettre):
    nouv_syll = False
    if syll[-1] in "aeiouy":
        if not lettre in "aeiouy":
            nouv_syll = True
    return nouv_syll

def nbr_syll_mot(mot):
    nbr_syll = 0
    syl = mot[0]
    for carac in mot:
        if est_ce_nouv_syll(syl, carac):
                nbr_syll += 1
                syl = ""
        syl += carac
    if syl[-1] in "aeiouy":
        nbr_syll += 1
    elif nbr_syll == 0:
        nbr_syll += 1
    return nbr_syll
    
def test_syll_mot():
    assert  nbr_syll_mot("tableau") == 2
    assert  nbr_syll_mot("ecouteur") == 3
    assert  nbr_syll_mot("e") == 1
    assert  nbr_syll_mot("ttttt") == 1
    assert  nbr_syll_mot("") == 0
    assert  nbr_syll_mot("anticonstitutionnel") == 7
test_syll_mot()

            