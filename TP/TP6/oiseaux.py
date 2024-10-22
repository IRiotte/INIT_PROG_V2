# --------------------------------------
# DONNEES
# --------------------------------------

# exemple de liste d'oiseaux observables
oiseaux = [("Merle", "Turtidé"), ("Moineau", "Passereau"), ("Mésange", "Passereau"),
           ("Pic vert", "Picidae"), ("Pie", "Corvidé"), ("Pinson", "Passereau"),
           ("Rouge-gorge", "Passereau"), ("Tourterelle", "Colombidé")] 

# exemples de listes de comptage ces listes ont la même longueur que oiseaux
comptage1 = [2, 5, 0, 1, 2, 0, 3, 5]
comptage2 = [2, 1, 3, 0, 0, 3, 5, 1]
comptage3 = [0, 0, 4, 3, 2, 1, 2, 4]

# exemples de listes d'observations. Notez que chaque liste correspond à la liste de comptage de
# même numéro
observations1 = [("Merle", 2), ("Moineau", 5), ("Pic vert", 1), ("Pie", 2),
                 ("Rouge-gorge", 3), ("Tourterelle", 5)]

observations2 = [("Merle", 2), ("Mésange", 1), ("Moineau", 3),
                 ("Pinson", 3), ("Tourterelle", 5), ("Rouge-gorge", 1)]

observations3 = [("Mésange", 4), ("Pic vert", 3), ("Pie", 2), ("Pinson", 1),
                 ("Rouge-gorge", 2), ("Tourterelle", 4)]


# --------------------------------------
# FONCTIONS
# --------------------------------------

def oiseau_le_plus_observe(liste_observations):
    """ recherche le nom de l'oiseau le plus observé de la liste
        (si il y en a plusieur on donne le 1er trouve)

    Args:
        liste_observations (list): une liste de tuples (nom_oiseau, nb_observes)

    Returns:
        str: l'oiseau le plus observé (None si la liste est vide)
    """
    oiseau_max = None
    if liste_observations != []:
        for observation in liste_observations:
            if oiseau_max is None or observation[1] > oiseau_max[1]:
                oiseau_max = observation
        return oiseau_max[0]
    return oiseau_max

def oiseau_le_plus_observe_bis(liste_observations):
    """ recherche le nom de l'oiseau le plus observé de la liste
        (si il y en a plusieur on donne le 1er trouve)

    Args:
        liste_observations (list): une liste de tuples (nom_oiseau, nb_observes)

    Returns:
        str: l'oiseau le plus observé (None si la liste est vide)
    """
    oiseau_max = None
    if liste_observations != []:
        for i in range(len(liste_observations)):
            if oiseau_max is None or liste_observations[i][1] > oiseau_max[1]:
                oiseau_max = liste_observations[i]
        return oiseau_max[0]
    return oiseau_max



def recherche_oiseau(nom, liste_oiseaux):
    for oiseau in liste_oiseaux:
        if nom == oiseau[0]:
            return oiseau
    return None

def recherche_par_famille(famille, liste_oiseaux):
    liste_meme_famille = []
    for oiseau in liste_oiseaux:
        if famille == oiseau[1]:
            liste_meme_famille.append(oiseau[0])
    return liste_meme_famille



def est_observation(liste_observation):
    return True

print(est_observation([("sdfs",485)]))




def moyenne_specimen(liste_observation):
    """Fonction qui calcul le nombre moyen de specimen dans une liste d'observation.

    Args:    liste_obs_oiseau = []
        liste_observation (list): une liste d'observation sous forme de tuple (nom, nbr_observe)

    Returns:
        float: la moyenne de specimen observés dans la liste, renvoie None s'il n'y a pas de
        specimen observé.

    Invariant:
        la variable nbr_obs contient le nombre d'observation totale pour tous les oiseaux déjà parcouru dans la liste
        la variable nbr_oiseau contient le nombre d'oiseaux observés pour tous les oiseaux déjà parcouru dans la liste.
    """

    nbr_obs = 0
    nbr_oiseau = 0
    for oiseau in liste_observation:
        nbr_obs += oiseau[1]
        nbr_oiseau += 1
    
    if nbr_oiseau > 0:
        return nbr_obs / nbr_oiseau
    return None



def total_obs_famille(nom_famille, liste_oiseaux, liste_observation):
    """Fonction qui renvoie le total d'obersvation pour une famille d'oiseaux
    donné.

    Args:
        nom_famille (str): _description_
        liste_oiseaux (list): une liste de tuple d'oiseaux de la forme (nom_oiseau, famille_oiseau)
        liste_observation (list): une liste de tuple d'observation de la forme (nom_oiseau, nbr_observation)

    Returns:
        int: Le total des observation pour une famille donné

    Invariant:
    """
    total_observe = 0
    liste_famille = recherche_par_famille(nom_famille, liste_oiseaux)
    for oiseau in liste_famille:
        total_observe += recherche_oiseau(oiseau, liste_observation)[1]
    return total_observe


# Exercice 4
#-----------------------------





#--------------------------------------
# PROGRAMME PRINCIPAL
#--------------------------------------

# afficher_graphique_observation(construire_liste_observations(oiseaux, comptage3))
# observes = saisie_observations(oiseaux)
# afficher_graphique_observation(observes)
# afficher_observations(oiseaux, observes)
