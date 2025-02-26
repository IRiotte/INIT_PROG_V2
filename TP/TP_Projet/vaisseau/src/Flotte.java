import java.util.List;
import java.util.ArrayList;

public class Flotte {
    private String nom;
    private List<Vaisseau> vaisseaux;

    public Flotte(){
        this.nom = "Nouvelle Flotte";
        this.vaisseaux = new ArrayList<>();
    }

    public Flotte(String nom){
        this.nom = nom;
        this.vaisseaux = new ArrayList<>();
    }


    public String getNom(){
        return this.nom;
    }

    public int nombreVaisseaux(){
        return this.vaisseaux.size();
    }

    public int totalPuissance(){
        int total = 0;
        for (Vaisseau vaisseau : this.vaisseaux) {
            total = total + vaisseau.getPuissance();
        }
        return total;
    }

    public void ajoute(Vaisseau vaisseau){
        this.vaisseaux.add(vaisseau);
    }

    public void ajoute(String nom, int puissance){
        this.vaisseaux.add(new Vaisseau(nom, puissance));
    }

    public void ajoute(String nom, int puissance, int nbrPassager){
        this.vaisseaux.add(new Vaisseau(nom, puissance, nbrPassager));
    }

    public int nombreDeVaisseauxSansPassagers(){
        int cpt = 0;
        for (Vaisseau vaisseau : this.vaisseaux) {
            if (vaisseau.getNombrePassagers() <= 0){
                cpt ++;
            }
        }
        return cpt;
    }

    public int puissanceDeFeuMax(){
        int max = 0;
        for (Vaisseau vaisseau : this.vaisseaux){
            if (vaisseau.getPuissance() > max) {
                max = vaisseau.getPuissance();
            }
        }
        return max;
    }

    public String nomDuVaisseauLeMoinsPuissant(){
        int min = 0;
        String nomMin = "";
        for (Vaisseau vaisseau : this.vaisseaux){
            if (min == 0 || vaisseau.getPuissance() < min){
                min = vaisseau.getPuissance();
                nomMin = vaisseau.getNom();
            }
        }
        return nomMin;
    }

}
