# liste de tuples (nom, prix)

def affiche_bilan_financier(week_end):

    dict_somme = {}
    somme_total = 0
    for (prenom, prix) in week_end:
        dict_somme[prenom] = dict_somme.get(prenom, 0) + prix
        somme_total += prix
    # suite de l'exo (la correction a été faite)