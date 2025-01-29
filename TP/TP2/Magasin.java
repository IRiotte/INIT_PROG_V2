public class Magasin{
    private String nom;
    private boolean ouvertLundi;
    private boolean ouvertDimanche;

    public Magasin(String nom, boolean lundi, boolean dimanche) {
        this.nom = nom;
        this.ouvertLundi = lundi;
        this.ouvertDimanche = dimanche;
    }

    public String getNom(){
        return this.nom;
    }

    public boolean estOuvertLundi(){
        return this.ouvertLundi;
    }

    public boolean estOuvertDimanche(){
        return this.ouvertDimanche;
    }

    @Override
    public String toString(){
        return this.nom + " lundi : " + ouvertLundi + " dimanche : " + ouvertDimanche;
    }
}