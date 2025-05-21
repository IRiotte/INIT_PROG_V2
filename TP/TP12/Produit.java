public class Produit {
    private String nom;
    private Double prix;

    public Produit(String nom, double prix) {
        this.nom = nom;
        this.prix = prix;
    }

    public String getNom() {
        return nom;
    }

    public double getPrix() {
        return prix;
    }



    @Override
    public boolean equals(Object obj) {
        if (this == obj) {return true;}
        if (obj == null || !(obj instanceof Produit)) {return false;}
        Produit produit = (Produit) obj;
        return this.nom.equals(produit.nom) && this.prix.equals(produit.prix);
    }

    @Override
    public int hashCode() {
        return nom.hashCode() * 1795 + prix.hashCode() * 611;
    }

    @Override
    public String toString() {
        return nom + " pour " + prix + " euro(s) ";
    }

}