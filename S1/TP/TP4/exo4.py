def commencement_mot(liste_mots, lettre):
    """Fonction qui renvoie une liste contenant tous les
    mots de une liste donnée commançant par une lettre donnée

    Args:
        liste_mots (list): liste de mots (str)
        lettre (str): une lettre

    Returns:
        list: la liste des mots (str) commençant
        une lettre donnée
    """    
    liste_lettre = []
    for mot in liste_mots:
        if mot[0] == lettre:
            liste_lettre.append(mot)
    return liste_lettre

def test_comm_mot():
    assert commencement_mot(["salut","hello","hallo","ciao","hola"], "h") == ["hello", "hallo", "hola"]
    assert commencement_mot(["salut","hello","hallo","ciao","hola"], "s") == ["salut"]
    assert commencement_mot([], "e") == []
    assert commencement_mot(["salut","hello","hallo","ciao","hola"], "k") == []

def commencement_mot_bis(liste_mots, lettre):
    liste_lettre = []
    for i in range(len(liste_mots)):
        if liste_mots[0][0] == lettre:
            liste_lettre.append(liste_mots[0])
    return liste_lettre