public class Lion extends Animal{
    private boolean  criniere;

    public Lion(String nom, double poids, boolean criniere) {
        super(nom, poids);
        this.criniere = criniere;
	}

	public Lion(String nom, double poids, Enclos enclos, boolean criniere) {
        super(nom, poids, enclos);
        this.criniere = criniere;
	}
	
    public boolean getCriniere() {
        return criniere;
    }

    public void setCriniere(boolean criniere) {
        this.criniere = criniere;
    }

    @Override
    public String emmettreUnSon(){
        return "rugissement";
    }
}
