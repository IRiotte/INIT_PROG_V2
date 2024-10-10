def somme_n_entier(n_ind):
    """Fonction qui renvoie la somme des n_ind premiers entiers.

    Args:
        n_ind (int): l'indice du dernier entier à calculer de 1 à celui-ci

    Returns:
        somme: la somme des n_ind premier entier
    """
    somme = 0
    for i in range(n_ind+1):
        somme += i
    return somme

def test_somm_n():
    assert somme_n_entier(0) == 0
    assert somme_n_entier(4) == 10
    assert somme_n_entier(5) == 15
    assert somme_n_entier(6) == 21

test_somm_n()



def term_suite_syracuse(val_init, ind_n):
    """Fonction qui renvoie la valeur du terme d'indice ind_n

    Args:
        terme0 (int): la valeur du premier terme de la suite
        ind_n (int): l'indice du terme de la suite à calculer

    Returns:
        int: _description_
    """
    val_suiv = val_init
    for i in range(ind_n):
        if val_suiv % 2 == 0:
            val_suiv = val_suiv / 2
        else:
            val_suiv = 3 * val_suiv + 1
    return val_suiv

print(term_suite_syracuse(0, 5))
print(term_suite_syracuse(1, 5))
print(term_suite_syracuse(78, 0))
print(term_suite_syracuse(2, 1))
print(term_suite_syracuse(3, 7))

def test_term_syr():
    assert term_suite_syracuse(0, 5) == 0
    assert term_suite_syracuse(1, 5) == 2
    assert term_suite_syracuse(78, 0) == 78
    assert term_suite_syracuse(2, 1) == 1
    assert term_suite_syracuse(3, 7) == 1

test_term_syr()