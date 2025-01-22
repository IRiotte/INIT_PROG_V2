from exo5 import carac_alph 
from exo4 import commencement_mot 


def liste_alpha_lettre(phrase, lettre):
    liste_mot = carac_alph(phrase)
    liste_mot_lettre = commencement_mot(liste_mot, lettre)
    return liste_mot_lettre

phrase1 = "Cela fait déjà 28 jours! 28 jours à l’IUT’O! Cool!!"

def test_list_alph_lett():
    assert liste_alpha_lettre(phrase1, "C") == ["Cela", "Cool"]