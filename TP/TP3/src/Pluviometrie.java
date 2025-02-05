import java.util.List;
import java.util.ArrayList;

public class Pluviometrie {
    private int annee;
    private int semaine;
    private List<Integer> precipitations;

    public Pluviometrie(int annee, int semaine){
        this.annee = annee;
        this.semaine = semaine;
        this.precipitations = new ArrayList<>();
        for (int i = 0; i<7; i++){
            this.precipitations.add(null);
        }
    }

    public void setPrecipitation(int jour, Integer pluie){
        this.precipitations.set(jour, pluie);
    }

    public Integer getPluie(int jour){
        return this.precipitations.get(jour);
    }

    public Integer quantiteTotal(){
        Integer somme = null;
        for (int i = 0 ; i<7; i++){
            if (this.precipitations.get(i) != null){
                if (somme == null){
                    somme = this.precipitations.get(i);
                }
                else{
                    somme += this.precipitations.get(i);
                }
            }
        }
        return somme;
    }


    public Integer quantiteMax() {
        Integer pluieMax = null;
        for (Integer pluie : this.precipitations){
            if (pluie != null){
                if (pluieMax == null || pluie > pluieMax){
                    pluieMax = pluie;
                }
            }
        }
        return pluieMax;
    }


    public boolean estPluvieuse(){
        Integer pluie1 = null;
        Integer pluie2 = null;
        for (int i = 1; i<7; ++i){
            pluie1 = this.precipitations.get(i-1);
            pluie1 = this.precipitations.get(i);
            if (pluie1 != null && pluie2 == null && pluie1 > 0 && pluie2 > 0){
                return true;
            }
        }
        return false;
    }


}
