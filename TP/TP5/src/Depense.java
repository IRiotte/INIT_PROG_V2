public class Depense{
    private double montant;
    private String produit;
    private Personne payeur;

    public Depense(Personne payeur, double montant, String produit){
        this.montant = montant;
        this.produit = produit;
        this.payeur = payeur;
    }

    public String getProduit(){
        return this.produit;
    }

    public double getMontant(){
        return this.montant;
    }

    public Personne getPayeur(){
        return this.payeur;
    }

}