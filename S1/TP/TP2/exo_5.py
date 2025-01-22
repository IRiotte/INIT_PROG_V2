def algo1(a, b, c, d):
    """Fonction qui renvoie le nombre minimum entre 4 nombres donnés

    Args:
        a (int): un nombre
        b (int): un nombre
        c (int): un nombre
        d (int): un nombre

    Returns:
        res (int): le plus petit nombre des 4 donnés en paramètre
    """    
    if a < b:
        res = a
    else:
        res = b
    if c < res:
        res = c
    if d < res:
        res = d
    return res

def algo2(m):
    """Fonction qui renvoie si un mot contient plus de voyelles que de consonnes, sinon renvoie faux

    Args:
        m (str): un mot en minuscule

    Returns:
        bool: si le mot m contient plus de voyelles que d'autres caractères ou pas
    """    
    res = 0
    for carac in m:
        if carac in "aeiouy":
            res += 1
        else:
            res -= 1
    return res>0

def test_algo1():
    assert algo1(8,1,6,4) == 1
    assert algo1(-1,7,9,5) == -1
    assert algo1(0,0,0,0) == 0
    assert algo1(7,6,5,4) == 4

def test_algo2():
    assert algo2("a") == True
    assert algo2("b") == False
    assert algo2("bcde") == False
    assert algo2("eyuf") == True
    assert algo2(" a e i") == False
    assert algo2("a'i' u") == False