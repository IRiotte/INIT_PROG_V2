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