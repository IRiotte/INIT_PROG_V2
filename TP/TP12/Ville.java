import java.util.*;

public class Ville {

    private String nom;
    private Set<Magasin> magasins;

    public Ville(String nom){
        this.nom = nom;
        this.magasins = new HashSet<>();
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
        for (Magasin magasin : this.magasins) {
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


}blanco