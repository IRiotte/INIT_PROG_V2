import java.util.List;
import java.util.ArrayList;

public class Cave {
    private List<Bouteille> bouteilles;

    public Cave(){
        this.bouteilles = new ArrayList<>();
    }


    public void ajouterBouteille(String region, String nom, int annee){
        
    }

    public int nbBouteilles(){
        return this.bouteilles.size();
    }

    public Bouteille plusVieilleBouteille(){
        Bouteille bouteilleMax = null;
        Integer anneeMax = null;
        int annee;
        for (Bouteille bouteille : this.bouteilles){
            annee = bouteille.getMillesime();
            if (anneeMax == null || anneeMax > annee){
                anneeMax = annee;
                bouteilleMax = bouteille;
            }
        }
        return bouteilleMax;
    }


    public boolean contient(String region, String nom, int annee){
        Bouteille bouteille = new Bouteille(region, nom, annee);
        return this.bouteilles.contains(bouteille);
    }


    public int nbBouteillesDeRegion(String region){
        return 0;
    }


    @Override
    public String toString(){
        return "Ma Cave : " + this.bouteilles;
    }



}
