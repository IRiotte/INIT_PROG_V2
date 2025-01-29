import java.util.ArrayList ;
import java.util.List ;

public class Ville {
    private String nom;
    private List<Magasin> magasins;
    public Ville(String nom){
        this.nom = nom;
        this.magasins = new ArrayList<>();
    }

    public void ajouteMagasin(Magasin magasin){
        this.magasins.add(magasin);
    }

    public void ajouteMagasin(String nom, boolean lundi, boolean dimanche) {
        Magasin newMagasin = new Magasin(nom, lundi, dimanche);
        this.magasins.add(newMagasin);
    }

    public List<Magasin> ouvertsLeLundi() {
        List<Magasin> listeOuvertLundi = new ArrayList<>();
        //for (Magasin magasin: this.magasins)
        for (int i=0; i<this.magasins.size(); i++){
            Magasin magasin =   this.magasins.get(i);
            if (magasin.estOuvertLundi()) {
                listeOuvertLundi.add(magasin);
            }
        }
        return listeOuvertLundi;
    }

    @Override
    public String toString() {
        String res = this.nom + " : \n";
        for (Magasin magasin : this.magasins){
            res = res + magasin.toString() + "\n";
        }
        return res;
    }
}