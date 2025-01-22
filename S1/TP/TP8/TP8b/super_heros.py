def intelligence_moyenne(dico_heros):
    """Fonction qui renvoie la moyenne d'intelligence des héros d'un dictionnaire

    Args:
        dico_heros (dict): le dictionnaire des héros avec clé: nom (str), valeur:tuple(force,int,desc)

    Returns:
        float: la moyenne d'intelligence des héros, None si il n'y en à pas
    """
    somme = 0
    nbr_heros = 0
    for _,intell,_ in dico_heros.values():
        somme += intell
        nbr_heros += 1
    if not nbr_heros == 0:
        return somme/nbr_heros
    return None

def kikelplusfort(dico_heros):
    """Fonction qui renvoie le héros le plus fort d'un dictionnaires de super héros

    Args:
        dico_heros (dict): le dictionnaire des héros avec clé: nom (str), valeur:tuple(force,int,desc)

    Returns:
        str: le nom du personnage le plus fort, None si le dictionnaire est vide.
    """
    le_plus_fort = None
    max_force = None
    for nom, (force,_,_) in dico_heros.items():
        if le_plus_fort is None or max_force < force:
            le_plus_fort = nom
            max_force = force
    return le_plus_fort

def combienDeCretins(dico_heros):
    """Fonction qui renvoie le nombre de personnages dont l'intelligence est strictement
    inférieure à la moyenne.

    Args:
        dico_heros (dict): le dictionnaire des héros avec clé: nom (str), valeur:tuple(force,int,desc)

    Returns:
        int: le nombre de personnages dont l'intelligence est strictement
    inférieure à la moyenne.
    """
    nbr_cretin = None
    moy_intell = intelligence_moyenne(dico_heros)
    for (_, intell, _) in dico_heros.values():
        if nbr_cretin is None:
            nbr_cretin = 0
        if intell < moy_intell:
            nbr_cretin += 1
    return nbr_cretin