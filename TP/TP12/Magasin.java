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

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        Magasin mag = (Magasin) obj;
        return ouvertLundi == mag.ouvertLundi &&
               ouvertDimanche == mag.ouvertDimanche &&
               nom.equals(mag.nom);
    }

    @Override
    public int hashCode() {
        int res = this.nom.hashCode() * 1759;
        if (this.ouvertLundi){
            res += 4943;
        }
        if (this.ouvertDimanche){
            res += 6911;
        }
        return res;
    }
}