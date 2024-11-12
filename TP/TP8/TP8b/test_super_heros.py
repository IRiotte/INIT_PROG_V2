import super_heros as sh

avengers1 = {
    "spiderman": (5,5,"araignée a quatre pattes"),
    "Hulk": (7,4,"Grand homme vert"),
    "Agent 13": (2,3,"agent 13"),
    "M Melin": (2,6,"expert en archi")
    }
dic_vide = dict()
avengers2 = {
    "Iron Man": (6,7,"araignée a quatre pattes"),
    "Cpt Amér": (5,4,"Grand homme vert"),
    "Ilane Riotte": (7,8,"eleve"),
    }
avengers3 = {"Python3": (1,9,"langage de prog")}

def test_intelligence_moyenne():
    assert sh.intelligence_moyenne(avengers1) == 4.5
    assert sh.intelligence_moyenne(dic_vide) is None
    assert sh.intelligence_moyenne(avengers2) == 19/3
    assert sh.intelligence_moyenne(avengers3) == 9.0

def test_kikelplusfort():
    assert sh.kikelplusfort(avengers1) == "Hulk"
    assert sh.kikelplusfort(dic_vide) is None
    assert sh.kikelplusfort(avengers2) == "Ilane Riotte"
    assert sh.kikelplusfort(avengers3) == "Python3"