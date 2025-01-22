#6.1 Entrée : sexe (str) 'homme' ou 'femme',
#             nb_course_gagne (int) le nombre de courses gagnées cette année,
#             tps_record (float) en seconde le record personnel,
#             champion_monde (bool) vrai si champion du monde
#             
#6.2 homme, 3, 11.6, False / femme, 2, 13.7, True
#    homme, 1, 26.7, False / femme, 4, 12.1, False
#
# algo: qualif_jo
#   entrée: sexe (str) 'homme' ou 'femme'
#           nb_course_gagne (int),
#           tps_record (float) en seconde,
#           champion_monde (bool) vrai si champion du monde
#   sortie: (bool) vrai si qualifié, faux sinon
#   Début:
#       si la personne est championne du monde alors
#           mettre Vrai dans qualifie
#       sinon
#           si elle a gagné au moins 3 courses alors
#               si c'est un homme alors
#                   si son record pesonnel est inférieur à 12sec alors
#                       mettre Vrai dans qualifie
#                   sinon
#                       mettre Vrai dans qualifie
#               sinon
#                   si son record personnel est inférieur à 15sec alors
#                       mettre Vrai dans qualifie
#                   sinon
#                       mettre Vrai dans qualifie
#           sinon 
#               mettre Vrai dans qualifie
#       retourner qualifie

def qualif_jo(sexe, nb_course_gagne, tps_record, champion_monde):
    """fonction qui renvoie si une personne est qualifié pour les jo ou pas

    Args:
        sexe (str): 'homme' ou 'femme'
        nb_course_gagne (int): nombres de course gagnées cette année
        tps_record (float): record personnel en seconde
        champion_monde (bool): True si champion du monde, False sinon

    Returns:
        bool: True si la personne est qualifiée au 100m des jo, False sinon
    """
    qualifie = False
    if champion_monde:
        qualifie = True
    elif nb_course_gagne >= 3:
        if sexe == 'homme':
            if tps_record < 12:
                qualifie = True
        elif tps_record < 15:
            qualifie = True
    return qualifie

def test():
    assert qualif_jo('homme', 3, 11.2, False)
    assert not qualif_jo('homme', 3, 12, False)
    assert not qualif_jo('homme', 2, 11.2, False)
    assert qualif_jo('homme', 2, 15, True)
    assert qualif_jo('femme', 3, 14.9, False)
    assert qualif_jo('femme', 3, 12.4, False)
    assert not qualif_jo('femme', 2, 13.5, False)
    assert qualif_jo('femme', 2, 15, True)
    