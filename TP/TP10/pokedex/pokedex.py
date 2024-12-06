"""Init Dev : TP10"""

# =====================================================================
# Exercice 1 : Choix de modélisation et complexité
# =====================================================================
# Modélisation n°1
# =====================================================================

# Penser à completer la fonction exemples_pokedex_v1 dans le fichier de tests

def appartient_v1(pokemon, pokedex): 
    """ renvoie True si pokemon (str) est présent dans le pokedex
    Invariant: Le pokemon n'a toujours pas été trouvé parmis les pokémons déjà parcourus
    Complexité: O(N) """
    for poke,_ in pokedex:
        if poke == pokemon:
            return True
    return False


def toutes_les_attaques_v1(pokemon, pokedex): 
    """
    param: un pokedex et le nom d'un pokemon (str) qui appartient au pokedex
    resultat: renvoie l'ensemble des types d'attaque du pokemon passé en paramètre
    Invariant: ens_att contient toute les attaques du pokemon pour chaque
    tuple (pokemon,attaque) déjà parcourus.
    Complexité: O(N) 
    """
    ens_att = set()
    for nom,att in pokedex:
        if nom == pokemon:
            ens_att.add(att)
    return ens_att



def nombre_de_v1(attaque, pokedex): 
    """
    param: un pokedex et un type d'attaque (str)
    resultat: renvoie le nombre de pokemons de ce type d'attaque
    dans le pokedex
    Invariant: ens_poke contient le nom des pokemon qui possèdent
    l'attaque donnée pour chaque pokémon déjà parcourus.
    Complexité: O(N) 
    """
    ens_poke = set()
    for nom,att in pokedex:
        if att == attaque:
            ens_poke.add(nom)
    return len(ens_poke) 


def attaque_preferee_v1(pokedex):
    """
    Renvoie le nom du type d'attaque qui est la plus fréquente dans le pokedex
    Invariant: dico_freq
    Complexité: O(N) 
    """
    dico_freq = dict()
    for _,att in pokedex:
        if att not in dico_freq:
            dico_freq[att] = 0
        dico_freq[att] += 1
    nbr_max = 0
    att_max = None
    for att,nbr_pok in dico_freq.items():
        if nbr_pok > nbr_max:
            nbr_max = nbr_pok
            att_max = att
    return att_max


# =====================================================================
# Modélisation n°2
# =====================================================================

# Penser à completer la fonction exemples_pokedex_v2 dans le fichier de tests

def appartient_v2(pokemon, pokedex):
    """ renvoie True si pokemon (str) est présent dans le pokedex 
    Invariant: Le pokemon n'a toujours pas été trouvé parmis les pokémons déjà parcourus
    Complexité: O(N) """
    return pokemon in pokedex


def toutes_les_attaques_v2(pokemon, pokedex):
    """
    param: un pokedex et le nom d'un pokemon (str) qui appartient au pokedex
    resultat: renvoie l'ensemble des types d'attaque du pokemon passé en paramètre
    Invariant: Le pokemon n'a toujours pas été trouvé parmis les pokémons déjà parcourus
    Complexité: O(N) 
    """
    if appartient_v2(pokemon,pokedex):
        return pokedex[pokemon]

def nombre_de_v2(attaque, pokedex):
    """
    param: un pokedex et un type d'attaque (str)
    resultat: renvoie le nombre de pokemons de ce type d'attaque
    dans le pokedex
    Invariant: Le pokemon n'a toujours pas été trouvé parmis les pokémons déjà parcourus
    Complexité: O(N) 
    """
    nbr_pok = 0
    for ens_att in pokedex.values():
        if attaque in ens_att:
            nbr_pok += 1
    return nbr_pok



def attaque_preferee_v2(pokedex):
    """
    Renvoie le nom du type d'attaque qui est la plus fréquente dans le pokedex
    Invariant: Le pokemon n'a toujours pas été trouvé parmis les pokémons déjà parcourus
    Complexité: O(N) 
    """
    dico_freq = dict()
    for nom,ens_att in pokedex.items():
        for att in ens_att:
            if att not in dico_freq:
                dico_freq[att] = 0
            dico_freq[att] += 1
    nbr_max = 0
    att_max = None
    for att,nbr_pok in dico_freq.items():
        if nbr_pok > nbr_max:
            nbr_max = nbr_pok
            att_max = att
    return att_max


# =====================================================================
# Modélisation n°3
# =====================================================================

# Penser à completer la fonction exemples_pokedex_v3 dans le fichier de tests


def appartient_v3(pokemon, pokedex):
    """ renvoie True si pokemon (str) est présent dans le pokedex 
    Invariant: Le pokemon n'a toujours pas été trouvé parmis les pokémons déjà parcourus
    Complexité: O(N) """
    for ens_pok in pokedex.values():
        if pokemon in ens_pok:
            return True
    return False


def toutes_les_attaques_v3(pokemon, pokedex):
    """
    param: un pokedex et le nom d'un pokemon (str) qui appartient au pokedex
    resultat: renvoie l'ensemble des types d'attaque du pokemon passé en paramètre
    Invariant: Le pokemon n'a toujours pas été trouvé parmis les pokémons déjà parcourus
    Complexité: O(N) 
    """
    ens_att = set()
    for att, ens_poke in pokedex.items():
        if pokemon in ens_poke:
            ens_att.add(att)
    return ens_att


def nombre_de_v3(attaque, pokedex):
    """
    param: un pokedex et un type d'attaque (str)
    resultat: renvoie le nombre de pokemons de ce type d'attaque
    dans le pokedex
    Invariant: Le pokemon n'a toujours pas été trouvé parmis les pokémons déjà parcourus
    Complexité: O(N) 
    """
    if attaque in pokedex:
        return len(pokedex[attaque])
    return 0


def attaque_preferee_v3(pokedex):
    """
    Renvoie le nom du type d'attaque qui est la plus fréquente dans le pokedex
    Invariant: Le pokemon n'a toujours pas été trouvé parmis les pokémons déjà parcourus
    Complexité: O(N) 
    """
    len_max = 0
    att_max = None
    for att,poke in pokedex.items():
        if len(poke) > len_max:
            len_max = len(poke)
            att_max = att
    return att_max

# =====================================================================
# Transformations
# =====================================================================

# Version 1 ==> Version 2

def v1_to_v2(pokedex_v1):
    """
    param: prend en paramètre un pokedex version 1
    renvoie le même pokedex mais en version 2
    Invariant: Le pokemon n'a toujours pas été trouvé parmis les pokémons déjà parcourus
    Complexité: O(N) 
    """
    pokedex_v2 = dict()
    for nom,att in pokedex_v1:
        if nom not in pokedex_v2:
            pokedex_v2[nom] = set()
        pokedex_v2[nom].add(att)
    return pokedex_v2

# Version 1 ==> Version 2

def v2_to_v3(pokedex_v2):
    """
    param: prend en paramètre un pokedex version2
    renvoie le même pokedex mais en version3
    Invariant: Le pokemon n'a toujours pas été trouvé parmis les pokémons déjà parcourus
    Complexité: O(N) 
    """
    pokedex_v3 = dict()
    for nom,ens_att in pokedex_v2.items():
        for att in ens_att:
            if att not in pokedex_v3:
                pokedex_v3[att] = set()
            pokedex_v3[att].add(nom)
    return pokedex_v3

