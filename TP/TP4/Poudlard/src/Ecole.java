import java.util.ArrayList;
import java.util.List;

public class Ecole {
    private String nom;
    private List<Maison> maisons;

    public Ecole(String nom) {
        this.nom = nom;
        this.maisons = new ArrayList<>();
    }

    public void ajouter(Maison maison) {
        this.maisons.add(maison);
    }

    public Maison plusGrandeMaison() {
        Integer max = null;
        Maison plusGrandeMaison = null;
        for (Maison maison : this.maisons) {
            if (plusGrandeMaison == null || maison.nombreEleves() > max) {
                plusGrandeMaison = maison;
                max = maison.nombreEleves();
            }
        }
        return plusGrandeMaison;
    }

    public List<Sorcier> LesCourageux(){
        List<Sorcier> listCourageux = new ArrayList<>();
        for (Maison maison : this.maisons){
            for (Sorcier sorcier : maison.getEleves()){
                if (sorcier.estCourageux()){listCourageux.add(sorcier);}
            }
        }
        return listCourageux;
    }

}
