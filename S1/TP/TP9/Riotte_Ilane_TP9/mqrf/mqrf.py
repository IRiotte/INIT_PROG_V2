
# ==========================
# La maison qui rend fou
# ==========================

def quel_guichet(mqrf, guichet):
    """Détermine le nom du guichet qui délivre le formulaire A-38

    Args:
        mqrf (dict): représente une maison qui rend fou
        guichet (str): le nom du guichet de départ qui est le nom d'un guichet de la mqrf

    Returns:
        str: le nom du guichet qui finit par donner le formulaire A-38
    """
    guichet_suiv = guichet
    while mqrf[guichet_suiv] is not None:
        guichet_suiv = mqrf[guichet_suiv]
    return guichet_suiv


def quel_guichet_v2(mqrf, guichet):
    """Détermine le nom du guichet qui délivre le formulaire A-38
    ainsi que le nombre de guichets visités

    Args:
        mqrf (dict): représente une maison qui rend fou
        guichet (str): le nom du guichet de départ qui est le nom d'un guichet de la mqrf

    Returns:
        tuple: le nom du guichet qui finit par donner le formulaire A-38 et le nombre de
        guichets visités pour y parvenir
    """
    guichet_suiv = guichet
    cpt = 1
    while mqrf[guichet_suiv] is not None:
        guichet_suiv = mqrf[guichet_suiv]
        cpt += 1
    return (guichet_suiv, cpt)


def quel_guichet_v3(mqrf, guichet):
    """Détermine le nom du guichet qui délivre le formulaire A-38
    ainsi que le nombre de guichets visités

    Args:
        mqrf (dict): représente une maison qui rend fou
        guichet (str): le nom du guichet de départ qui est le nom d'un guichet de la mqrf

    Returns:
        tuple: le nom du guichet qui finit par donner le formulaire A-38 et le nombre de
        guichets visités pour y parvenir
        S'il n'est pas possible d'obtenir le formulaire en partant du guichet de depart,
        cette fonction renvoie None
    """
    guichet_suiv = guichet
    cpt = 1
    depasse = False
    while mqrf[guichet_suiv] is not None and not depasse:
        guichet_suiv = mqrf[guichet_suiv]
        cpt += 1
        if cpt > len(mqrf):
            depasse = True
    if depasse:
        return None
    else:
        return (guichet_suiv, cpt)


