

def mystere(liste, valeur):
    """Fonction qui renvoie le nombre d'éléments juste avant la 4e occurrence d'une valeur
    dans une liste, et None si elle est présente moins de 4 fois.

    Args:
        liste (list): une liste d'éléments de type quelconque.
        valeur (elem): un élément de type quelconque.

    Returns:
        int: le nombre d'élément juste avant la 4e occurrence de la valeur dans la liste,
        None si elle apparaît moins de 4 fois.
    """
    xxx = 0 #contient le nombre d'éléments déja parcourus à chaque tour de boucle
    yyy = 0 #contient le nombre d'occurence d'une valeur dans les valeurs de la liste déjà parcourues
    for elem in liste:
        if elem == valeur:
            yyy += 1
            if yyy > 3:
                return xxx #la liste contient plus de 3 fois l'élément "valeur" donné en paramètre
        xxx += 1
    return None


assert mystere([12, 5, 8, 48, 12, 418, 185, 17, 5, 87], 20) is None
assert mystere([5, 12, 5, 8, 48, 5, 12, 418, 185, 17, 5, 87], 5) == 10

def mystere_ind(liste, valeur):
    """Fonction qui renvoie à partir de combien d'élément une valeur apparaît strictement
    plus de 3 fois dans une liste, et renvoie None si elle n'apparaît pas plus de 3 fois.

    Args:
        liste ([list): une liste d'éléments de type quelconque.
        valeur (elem): un élément de type quelconque.

    Returns:
        int: le nombre d'élément à partir duquel la valeur 
    """
    xxx = 0 #contient le nombre d'éléments déja parcourus à chaque tour de boucle
    yyy = 0 #contient le nombre d'occurence d'une valeur dans les valeurs de la liste déjà parcourues
    for i in range(len(liste)):
        if liste[i] == valeur:
            yyy += 1
            if yyy > 3:
                return xxx #la liste contient plus de 3 fois l'élément "valeur" donné en paramètre
        xxx += 1
    return None


assert mystere_ind([12, 5, 8, 48, 12, 418, 185, 17, 5, 87], 20) is None
assert mystere_ind([5, 12, 5, 8, 48, 5, 12, 418, 185, 17, 5, 87], 5) == 10