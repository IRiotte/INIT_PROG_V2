def meilleur_score(liste_joueur, liste_score, joueur):
    """Fonction qui renvoie le meilleur score d'un joueur s'il est présent
    dans la liste, sinon renvoie None

    Args:
        liste_joueur (liste): la liste des prénoms des joueurs, en fonction
        de leur score. est de même taille que lsite_score
        liste_score (list): la liste des score des joueurs. est de mâme taille
        que liste_joueur
        joueur (str): le nom d'un joueur

    Returns:
        int: le meilleur score du joueur donné en paramètres,
        renvoie None s'il n'est pas dans la liste des joueur
    """
    if joueur in liste_joueur:
        max_score = 0
        for i in range(len(liste_joueur)):
            if liste_joueur[i] == joueur:
                if liste_score[i] > max_score:
                    max_score = liste_score[i]
        return max_score
    
# ---------------------------------------
# Exemple de scores
# ---------------------------------------
scores = [352100, 325410, 312785, 220199, 127853]
joueurs = ['Batman', 'Robin', 'Batman', 'Batman', 'Joker']

def test_max_score():
    assert meilleur_score(joueurs, scores, "Batman") == 352100
    assert meilleur_score(joueurs, scores, "Robin") == 325410
    assert meilleur_score(joueurs, scores, "Joker") == 127853
    assert meilleur_score(joueurs, scores, "Bob") is None


#4.2

def est_score_decroissant(liste_score):
    """Fonction qui renvoie si une liste de score est triée dans l'ordre
    décroissant.

    Args:
        liste_score (list): la liste de score qui contient des entier (int)

    Returns:
        bool: renvoie True si la liste est triée dans l'ordre décroissant,
        False sinon.

    Invariant: La liste est triée dans l'ordre croissant jusqu'à l'indice i exclu.
    """    
    for i in range(1, len(liste_score)):
        if liste_score[i-1] < liste_score[i]:
            return False
    return True

score1 = [100, 50, 25, 12, 6]
score2 = [100, 50, 80, 20, 1]
score3 = [80, 100, 120]
score4 = [9, 8, 7, 6, 10]
score5 = []
score6 = [1]

def test_score_decr():
    assert est_score_decroissant(score1)
    assert not est_score_decroissant(score2)
    assert not est_score_decroissant(score3)
    assert not est_score_decroissant(score4)
    assert est_score_decroissant(score5)
    assert est_score_decroissant(score6)


#4.3

def nbr_fois_joueur_present(liste_joueur, nom_joueur):
    """Fonction qui renvoie le nombre de fois qu'un joueur est present
    dans la liste des meilleurs scores.

    Args:
        liste_joueur (list): la liste des joueur ayant les melleurs scores
        nom_joueur (str): le nom du joueur à rechercher

    Returns:
        int: renvoie le nombre de fois où le nom apparaît dans la liste des joueur ayant les
        meilleurs scores
    
    Invariant: nb_fois contient le nombre de fois que le nom du joueur apparraît dans les
    noms des joueurs déjà parcourus.
    """  
    nbr_fois = 0  
    for joueur in liste_joueur:
        if joueur == nom_joueur:
            nbr_fois += 1
    return nbr_fois


def test_nbr_joueur():
    assert nbr_fois_joueur_present(joueurs, "Robin") == 1
    assert nbr_fois_joueur_present(joueurs, "Joker") == 1
    assert nbr_fois_joueur_present(joueurs, "Batman") == 3
    assert nbr_fois_joueur_present(joueurs, "skhdfieu") == 0
    assert nbr_fois_joueur_present(joueurs, "") == 0
    assert nbr_fois_joueur_present([], "Batman") == 0


#4.4

def meilleur_score_joueur(liste_joueur,liste_score, joueur):
    """Fonction qui renvoie le meilleur score d'un joueur donné en paramètre s'il est présent dans la liste.

    Args:
        liste_joueur (list): la liste des joueurs ayant les meilleurs scores
        liste_score (list): la liste des meilleurs scores de même taille que la liste des joueurs
        joueur (str): le nom du joueur dont on veut connaître le meilleur score

    Returns:
        int: le meilleur score du joueur dans la liste des meilleurs scores s'il est présent dans la liste,
        sinon renvoie None

    Invariant: score contient le meilleur score du joueur pour tous les scores s'il 
    est présent dans la liste déjà parcourus
    """    
    max_score = None
    for i in range(len(liste_joueur)):
        if liste_joueur[i] == joueur:
            return liste_score[i] 
    return max_score


scores1 = [1500, 800, 680, 250, 100]
joueurs2 = ['Robin', 'Batman', 'Batman', 'Batman', 'Joker']

def test_meilleur_score():
    assert meilleur_score_joueur(joueurs2, scores1,"Batman") == 800
    assert meilleur_score_joueur(joueurs2, scores1,"Joker") == 100
    assert meilleur_score_joueur(joueurs2, scores1,"Robin") == 1500
    assert meilleur_score_joueur(joueurs2, scores1,"asterix") is None



#4.5

def ind_inserer(liste_score, score):
    """Fonction qui renvoie l'indice dans la liste de scores où on pourra insérer le score
    donnée en paramètre

    Args:
        liste_score (liste): la liste des scores trié dans l'ordre décroissant
        score (int): le score avec lequel on voudrait trouver l'indice pour l'insérer

    Returns:
        int: renvoie l'indice de la position à laquelle on pourra intégrer le score donné
        en paramètre.

    Invariant: pour tous les scores déjà parcourus, les score sont supérieur au score donné
    en paramètre
    """
    for i in range(len(liste_score)):
        if liste_score[i] < score:
            return i
    return len(liste_score)

def test_ind_inserer():
    assert ind_inserer([5,3,2,1], 4) == 1
    assert ind_inserer([4,3,2,1], 0) == 4
    assert ind_inserer([4,3,2,1], 5) == 0
    assert ind_inserer([], 3) == 0
    assert ind_inserer([6,5,5,1], 5) == 3


#4.6

def inserer_score(score, auteur, liste_joueur, liste_score):
    """_summary_

    Args:
        score (_type_): _description_
        auteur (_type_): _description_
        liste_joueur (_type_): _description_
        liste_score (_type_): _description_
    """    
    pass
