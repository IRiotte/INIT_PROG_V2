"""
Init Dev : TP10
Exercice 2 : Ecosystème
"""

def extinction_immediate(ecosysteme, animal):
    """
    renvoie True si animal s'éteint immédiatement dans l'écosystème faute
    de nourriture
    """
    nourriture = ecosysteme[animal]
    if not nourriture is None:
        return (not nourriture in ecosysteme)
    return False

def en_voie_disparition(ecosysteme, animal):
    """
    renvoie True si animal s'éteint est voué à disparaitre à long terme
    """
    i = 0
    present = True
    temp_animal = animal
    while i < len(ecosysteme) and present and not temp_animal is None:
        if extinction_immediate(ecosysteme, temp_animal):
            present = False
        else:
            temp_animal = ecosysteme[temp_animal]
            i +=1
    return not present

def animaux_en_danger(ecosysteme):
    """ renvoie l'ensemble des animaux qui sont en danger d'extinction immédiate"""
    ens = set()
    for animal in ecosysteme:
        if not animal in ens:
            if extinction_immediate(ecosysteme, animal):
                ens.add(animal)
    return ens

def especes_en_voie_disparition(ecosysteme):
    """ renvoie l'ensemble des animaux qui sont en voués à disparaitre à long terme
    """
    ens = set()
    for animal in ecosysteme:
        if not animal in ens:
            if en_voie_disparition(ecosysteme, animal):
                ens.add(animal)
    return ens



