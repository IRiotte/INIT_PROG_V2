def carac_alph(phrase):
    liste_cara_alph = []
    chaine_temp = ""
    for carac in phrase:
        if carac.isalpha():
            chaine_temp += carac
        elif not chaine_temp == "":
            liste_cara_alph.append(chaine_temp)
            chaine_temp = ""
    if not phrase == "":
        if phrase[-1].isalpha():
            liste_cara_alph.append(chaine_temp)
    return liste_cara_alph

def test_chaine_alpha():
    assert carac_alph("Cela fait déjà 28 jours!") == ["Cela", "fait", "déjà", "jours"]
    assert carac_alph("(3*2)/1") == []
    assert carac_alph("") == []
    assert carac_alph("lll") ==["lll"]
    assert carac_alph("l    h") == ["l", "h"]
    assert carac_alph("    h") == ["h"]
    assert carac_alph("l'e'r't'y") == ["l","e","r","t","y"]
    assert carac_alph("l,e,r,t,y") == ["l","e","r","t","y"]


