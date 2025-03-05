import java.util.List;
import java.util.ArrayList;

class Texte {
    private List<Lettre> unTexte;

    public Texte(String chaine) {
		unTexte = new ArrayList<>(); 
	   	Lettre l; 
	   	for(int i = 0; i < chaine.length(); ++i) {
			l = new Lettre(chaine.charAt(i));
            unTexte.add(l); 
		}
	}

	@Override
    public String toString() {
		return unTexte.toString(); 
    }

	/**
	 * renvoie le texte en morse
	 * @return String renvoie un teste en morse
	 */
    public String toMorse() {
		String leMorse = "";
		Lettre lettre;
		Lettre prec = null;
		for(int i = 0; i < unTexte.size(); ++i) {
	    	lettre = unTexte.get(i);
	    	leMorse += lettre.toMorse();
			// séparateur de lettre dans un mot ___
			if (i < unTexte.size() -1) {
				// ne pas ajouter de séparateur devant un blanc
				if (prec == null || prec.toChar() == ' ') {
					if (lettre.toChar() != ' ') {
						leMorse += "___";
					}
			    }
			}
			prec = lettre;
		} 
		return leMorse;
	}

	/**
	 * 
	 * @param lettre une lettre 
	 * @return boolean qui test si un texte contient
	 * cette lettre 
	 */
	public boolean contient(Lettre lettre) {
		return this.unTexte.contains(lettre);
		// redéfinir equals sur Lettre
	}

// A AMELIORER 
	public String decode(String texteEnMorse) {
		char unCarac;
		String uneLettre = "";
		int nbTirets = 0;
		Lettre lettre = null;
		String texteDecode = "";
		int longueurTexte = texteEnMorse.length();
		boolean reinitialise = false;
		for (int i = 0; i< longueurTexte; ++i) {
			unCarac = texteEnMorse.charAt(i);
			if (unCarac != '_') {
				uneLettre += unCarac;
				// accumuler les caractère d'une lettre
			}
			else {
				++nbTirets;
			}
			
			if (nbTirets == 3) {
				// on a trouvé une lettre 
				// on regarde le suivant si pas tiret
				if (i != longueurTexte - 1 &&
					texteEnMorse.charAt(i+1) != '_') {
						lettre = new Lettre(uneLettre); 
						texteDecode += lettre.toChar();
						reinitialise = true;
				}
				// tester si pas encore un autre tiret
			}

			if (nbTirets == 7) {
				// un blanc 
				lettre = new Lettre(uneLettre);
				texteDecode += lettre.toChar();
				texteDecode += ' ';
				reinitialise = true;
			}
			
			if (nbTirets == 1) {
				// pas d'autre ?
				if (i != longueurTexte -1 &&
				    texteEnMorse.charAt(i+1) != '_') {
						// on est dans une lettre
						uneLettre += '_';
						nbTirets = 0;
				} 
			}
			
			if (reinitialise) {
				// réinitialiser les variables 
				uneLettre = "";
				nbTirets = 0;
				reinitialise = false;
			}
		}
	
	// ajout de la dernière lettre car pas de blanc ! 
	lettre = new Lettre(uneLettre);
	texteDecode += lettre.toChar();	
	return texteDecode;
	}
}