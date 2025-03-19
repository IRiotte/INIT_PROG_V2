public abstract class Animal {
    private String nom;
    private double poids;
    private Enclos enclos;

    protected Animal(String nom, double poids) {
        this.nom = nom;
        this.poids = poids;
        this.enclos = null;
    }

    protected Animal(String nom, double poids, Enclos enclos) {
        this.nom = nom;
        this.poids = poids;
        this.enclos = enclos;
    }

    public String getNom() {
        return nom;
    }

    public double getPoids() {
        return poids;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public void setPoids(double poids) {
        this.poids = poids;
    }

    public Enclos getEnclos() {
        return enclos;
    }

    public void setEnclos(Enclos enclos) {
        this.enclos = enclos;
    }

    @Override
    public String toString(){
        return this.nom + " pèse " + this.poids + " kg";
    }

    
    @Override
    public boolean equals(Object objet){
        if (objet == null) {return false;}
        if (objet == this) {return true;}
        if (! (objet instanceof Animal)) {return false;}
    
        Animal tmp = (Animal) objet;
        return this.nom.equals(tmp.nom) 
        && this.poids == tmp.poids; 
    }
}
