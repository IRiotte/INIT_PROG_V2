def chiffre_in_chaine(chaine):
    for i in range(len(chaine)):
        if chaine[i] in "0123456789":
            return i

def test_chiff_ch():       
    assert chiffre_in_chaine("on est le 30/09/2021" ) == 10
    assert chiffre_in_chaine("on est 1" ) == 7
    assert chiffre_in_chaine("30/09/2021" ) == 0
    assert chiffre_in_chaine("" ) is None
    assert chiffre_in_chaine("on est le dix-huit" ) is None


def pop_ville(liste_ville, liste_pop, nom_ville):
    if nom_ville in liste_ville:
        for i in range(len(liste_ville)):
            if nom_ville == liste_ville[i]:
                return liste_pop[i]


# --------------------------------------
# Exemple de villes avec leur population
# --------------------------------------
liste_villes = ["Blois", "Bourges", "Chartres", "Châteauroux", "Dreux",
                "Joué-lès-Tours", "Olivet", "Orléans", "Tours", "Vierzon"]
population = [45871, 64668,  38426, 43442, 30664, 38250, 22168, 116238,
              136463,  25725]


def test_pop_ville():
    assert pop_ville(liste_villes, population, "Blois") == 45871
    assert pop_ville(liste_villes, population, "Vierzon") == 25725
    assert pop_ville(liste_villes, population, "Chartres") == 38426
    assert pop_ville(liste_villes, population, "Orléans") == 116238
    assert pop_ville(liste_villes, population, "super ville") is None

