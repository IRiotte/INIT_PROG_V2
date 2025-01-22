#Exercice 2:


def pop_max_ville(liste_villes, population):
    """Fonction qui renvoie le nom de la ville la plus peuplée de la liste
     partir de la liste de leurs population triée dans le même ordre

    Args:
        liste_villes (list): liste des noms de différentes villes (str)
        population (list): liste des population rangée dans le même ordre
                            que la liste des ville

    Returns:
        str: Le nom de la ville la plus peupée de la liste
    """
    if not liste_villes == []:
        max_pop_ind = 0
        for i in range(len(population)):
            if population[i] > population[max_pop_ind]:
                max_pop_ind = i
        
        vill_max = liste_villes[max_pop_ind]
    else:
        vill_max = None
    return vill_max


# --------------------------------------
# Exemple de villes avec leur population
# --------------------------------------
liste_villes = ["Blois", "Bourges", "Chartres", "Châteauroux", "Dreux",
                "Joué-lès-Tours", "Olivet", "Orléans", "Tours", "Vierzon", "La-Ferté-Saint-Aubin"]
population = [45871, 64668,  38426, 43442, 30664, 38250, 22168, 116238, 136463,
              25725, 8456]

liste_villes1 = ["Orléans", "Blois", "Bourges", "Chartres", "Châteauroux", "Dreux",
                "Joué-lès-Tours", "Olivet", "Vierzon"]
population1 = [116238, 45871, 64668,  38426, 43442, 30664, 38250, 22168, 
              25725]

def test_max_pop():
    assert pop_max_ville(liste_villes, population) == "Tours"
    assert pop_max_ville(liste_villes1, population1) == "Orléans"
    assert pop_max_ville([], []) == None