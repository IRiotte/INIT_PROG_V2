def trouver_dans_liste(liste, cible):
    indice = 0
    trouve = False
    while indice < len(liste) and not trouve:
        if liste[indice] == cible:
            trouve = True
        indice += 1
    return trouve


def cumuler_jusqu_a_seuil(dictionnaire, seuil):
    total = 0
    au_dessus_seuil = False
    for cle, valeur in dictionnaire.items():
        if not au_dessus_seuil and not total >= seuil:
            total += valeur
        else:
            au_dessus_seuil = True
    return total



courses_morticia = ["bave de crapeau", "oeufs de dragon", "lézards",
                    "ketchup", "sel" ]
facture_morticia = [17, 157, 17, 2, 1]

def ajout_article(liste_course):
    