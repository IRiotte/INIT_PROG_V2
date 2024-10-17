import oiseaux
# --------------------------------------
# FONCTIONS
# --------------------------------------

def test_recherche_oiseau():
    assert oiseaux.recherche_oiseau("Moineau",oiseaux.oiseaux)==("Moineau", "Passereau")
    assert oiseaux.recherche_oiseau("Tourterelle",oiseaux.oiseaux)==("Tourterelle", "Colombidé")
    assert oiseaux.recherche_oiseau("Mésange",oiseaux.oiseaux)==("Mésange", "Passereau")
    assert oiseaux.recherche_oiseau("",oiseaux.oiseaux) is None

def test_recherche_par_famille():
    assert oiseaux.recherche_par_famille("Colombidé",oiseaux.oiseaux)==["Tourterelle"]
    assert oiseaux.recherche_par_famille("Passereau",oiseaux.oiseaux)==["Moineau", "Mésange", "Pinson", "Rouge-gorge"]
    assert oiseaux.recherche_par_famille("Turtidé",oiseaux.oiseaux)==["Merle"]
    assert oiseaux.recherche_par_famille("",oiseaux.oiseaux) == []

def test_oiseau_le_plus_observe():
    assert oiseaux.oiseau_le_plus_observe(oiseaux.observations1)=="Moineau"
    assert oiseaux.oiseau_le_plus_observe(oiseaux.observations2)=="Tourterelle"
    assert oiseaux.oiseau_le_plus_observe(oiseaux.observations3)=="Mésange"
    assert oiseaux.oiseau_le_plus_observe([])==None
def test_oiseau_le_plus_observe_bis():
    assert oiseaux.oiseau_le_plus_observe_bis(oiseaux.observations1)=="Moineau"
    assert oiseaux.oiseau_le_plus_observe_bis(oiseaux.observations2)=="Tourterelle"
    assert oiseaux.oiseau_le_plus_observe_bis(oiseaux.observations3)=="Mésange"
    assert oiseaux.oiseau_le_plus_observe_bis([])==None

def test_est_liste_observations():
    assert oiseaux.est_liste_observations(...)==...

def test_max_observations():
    assert oiseaux.max_observations(...)==...

def test_moyenne_oiseaux_observes():
    assert oiseaux.moyenne_oiseaux_observes(...)==...

def test_total_famille():
    assert oiseaux.total_famille(...)==...


def test_construire_liste_observations():
    assert oiseaux.construire_liste_observations(...)==...

def test_creer_ligne_sup():
    assert oiseaux.creer_ligne_sup(...)==...

def test_creer_ligne_noms_oiseaux():
    assert oiseaux.creer_ligne_noms_oiseaux(...)==...
