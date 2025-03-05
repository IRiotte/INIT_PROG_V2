public class Sorcier {
    private String nom;
    private int courage;
    private int sagesse;
    
    public Sorcier(String nom, int courage, int sagesse) {
        this.nom = nom;
        this.courage = courage;
        this.sagesse = sagesse;
    }

    public String getNom() {
        return nom;
    }

    public int getCourage() {
        return courage;
    }

    public int getSagesse() {
        return sagesse;
    }

    public boolean estCourageux() {
        return courage > 8;
    }


}