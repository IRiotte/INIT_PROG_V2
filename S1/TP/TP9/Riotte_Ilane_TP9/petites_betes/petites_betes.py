"""Init Dev : TP9"""



# ==========================
# Petites bêtes (la suite)
# ==========================

def toutes_les_familles_v2(pokedex):
    """détermine l'ensemble des familles représentées dans le pokedex

    Args:
        pokedex (dict): un dictionnaire dont les clés sont les noms de pokemons et la
        valeur associée l'ensemble (set) de ses familles (str)

    Returns:
        set: l'ensemble des familles représentées dans le pokedex
    """
    liste_famille =  set()
    for famille in pokedex.values():
        liste_famille = liste_famille | famille
    return liste_famille

def nombre_pokemons_v2(pokedex, famille):
    """calcule le nombre de pokemons d'une certaine famille dans un pokedex

    Args:
        pokedex (dict): un dictionnaire dont les clés sont les noms de pokemons et la
        valeur associée l'ensemble (set) de ses familles (str)
        famille (str): le nom de la famille concernée

    Returns:
        int: le nombre de pokemons d'une certaine famille dans un pokedex
    """
    nbr_occur_fam = 0
    for ensemble_famille in pokedex.values():
        for pok_famille in ensemble_famille:
            if famille == pok_famille:
                nbr_occur_fam += 1
    return nbr_occur_fam

def frequences_famille_v2(pokedex):
    """Construit le dictionnaire de fréqeunces des familles d'un pokedex

    Args:
        pokedex (dict): un dictionnaire dont les clés sont les noms de pokemons et la
        valeur associée l'ensemble (set) de ses familles (str)

    Returns:
        dict: un dictionnaire dont les clés sont le nom de familles (str) et la valeur
        associée est le nombre de représentants de la famille (int)
    """
    dico_freq_famille = {}
    for ensemble_famille in pokedex.values():
        for famille in ensemble_famille:
            if famille not in dico_freq_famille:
                dico_freq_famille[famille] = 0
            dico_freq_famille[famille] += 1
    return dico_freq_famille

def dico_par_famille_v2(pokedex):
    """Construit un dictionnaire dont les les clés sont le nom de familles (str)
    et la valeur associée est l'ensemble (set) des noms des pokemons de
    cette famille dans le pokedex

    Args:
        pokedex (dict): un dictionnaire dont les clés sont les noms de pokemons et la
        valeur associée l'ensemble (set) de ses familles (str)

    Returns:
        dict: un dictionnaire dont les clés sont le nom de familles (str) et la valeur associée est
        l'ensemble (set) des noms des pokemons de cette famille dans le pokedex
    """
    dico_famille = {}
    for pokemon,ensemble_famille in pokedex.items():
        for famille in ensemble_famille:
            if famille not in dico_famille:
                dico_famille[famille] = set()
            dico_famille[famille].add(pokemon)
    return dico_famille

def famille_la_plus_representee_v2(pokedex):
    """détermine le nom de la famille la plus représentée dans le pokedex

    Args:
        pokedex (dict): un dictionnaire dont les clés sont les noms de pokemons et la
        valeur associée l'ensemble (set) de ses familles (str)

    Returns:
        str: le nom de la famille la plus représentée dans le pokedex
    """
    dico_freq = frequences_famille_v2(pokedex)
    famille_max = None
    for famille,freq in dico_freq.items():
        if famille_max is None or dico_freq[famille_max] < freq:
            famille_max = famille
    return famille_max
