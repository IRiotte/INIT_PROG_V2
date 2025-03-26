public class Serpent extends Animal{
    private boolean venimeux;

    public Serpent(String nom, double poids, boolean venimeux) {
        super(nom, poids);
        this.venimeux = venimeux;
	}

	public Serpent(String nom, double poids, Enclos enclos, boolean venimeux) {
        super(nom, poids, enclos);
        this.venimeux = venimeux;
	}
	
    public boolean getVenimeux() {
        return venimeux;
    }

    public void setVenimeux(boolean venimeux) {
        this.venimeux = venimeux;
    }

    @Override
    public String emmettreUnSon(){
        return "sifflement";
    }
}
