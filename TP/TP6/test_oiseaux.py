import oiseaux as ois
# --------------------------------------
# FONCTIONS
# --------------------------------------

def test_recherche_oiseau():
    assert ois.recherche_oiseau("Moineau",ois.oiseaux)==("Moineau", "Passereau")
    assert ois.recherche_oiseau("Tourterelle",ois.oiseaux)==("Tourterelle", "Colombidé")
    assert ois.recherche_oiseau("Mésange",ois.oiseaux)==("Mésange", "Passereau")
    assert ois.recherche_oiseau("",ois.oiseaux) is None

def test_recherche_par_famille():
    assert ois.recherche_par_famille("Colombidé",ois.oiseaux)==["Tourterelle"]
    assert ois.recherche_par_famille("Passereau",ois.oiseaux)==["Moineau", "Mésange", "Pinson", "Rouge-gorge"]
    assert ois.recherche_par_famille("Turtidé",ois.oiseaux)==["Merle"]
    assert ois.recherche_par_famille("",ois.oiseaux) == []

def test_oiseau_le_plus_observe():
    assert ois.oiseau_le_plus_observe(ois.observations1)=="Moineau"
    assert ois.oiseau_le_plus_observe(ois.observations2)=="Tourterelle"
    assert ois.oiseau_le_plus_observe(ois.observations3)=="Mésange"
    assert ois.oiseau_le_plus_observe([])==None
def test_oiseau_le_plus_observe_bis():
    assert ois.oiseau_le_plus_observe_bis(ois.observations1)=="Moineau"
    assert ois.oiseau_le_plus_observe_bis(ois.observations2)=="Tourterelle"
    assert ois.oiseau_le_plus_observe_bis(ois.observations3)=="Mésange"
    assert ois.oiseau_le_plus_observe_bis([])==None

def test_est_liste_observations():
    assert ois.est_liste_observations(ois.observations1)
    assert ois.est_liste_observations(ois.observations2)
    assert ois.est_liste_observations(ois.observations3)
    assert not ois.est_liste_observations([("aaa", 0)])
    assert not ois.est_liste_observations([("bbb", 4), ("aaa", 17)])

def test_max_observations():
    assert ois.max_observations(ois.observations1)==...
    assert ois.max_observations(ois.observations2)==...
    assert ois.max_observations(ois.observations3)==...
    assert ois.max_observations([]) is None

def test_moyenne_specimen():
    assert ois.moyenne_specimen(ois.observations1)==3.0
    assert ois.moyenne_specimen(ois.observations2)==2.5
    assert ois.moyenne_specimen(ois.observations3)== 16/6
    assert ois.moyenne_specimen([("sdfqef", 15)])==15.0
    assert ois.moyenne_specimen([("sdfqef", 0)])==0.0
    assert ois.moyenne_specimen([]) is None

def test_total_famille():
    assert ois.total_obs_famille("Passereau", ois.oiseaux, ois.observations1)==8
    assert ois.total_obs_famille("Colombidé", ois.oiseaux, ois.observations2)==5
    assert ois.total_obs_famille("Passereau", ois.oiseaux, ois.observations3)==7
    assert ois.total_obs_famille("Labrador", ois.oiseaux, ois.observations3)==0


def test_construire_liste_observations():
    assert ois.construire_liste_observations(...)==...

def test_creer_ligne_sup():
    assert ois.creer_ligne_sup(...)==...

def test_creer_ligne_noms_oiseaux():
    assert ois.creer_ligne_noms_oiseaux(...)==...
