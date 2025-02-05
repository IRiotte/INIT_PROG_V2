import java.util.List;
import java.util.ArrayList;

public class Table {

    private List<Personne> lesConvives;

    public Table(){
        this.lesConvives = new ArrayList<>();
    }

    public void ajouteConvive(String nom, int age){
        Personne convive = new Personne(nom, age);
        this.lesConvives.add(convive);
    }

    public double moyenneAge(){
        double somme = 0;
        for (Personne convive : this.lesConvives){
            somme += convive.getAge();
        }
        return somme/this.lesConvives.size();
    }

    public int nombreDAdultes(){
        int nbAdulte = 0;
        for (Personne personne : this.lesConvives){
            if (personne.getAge() >= 18){
                nbAdulte ++;
            }
        }
        return nbAdulte;
    }

    public String lePlusJeune(){
        String nomPlusJeune = "";
        int agePlusJeune = 0;
        for (Personne personne : this.lesConvives){
            if (agePlusJeune == 0){
                agePlusJeune = personne.getAge();
                nomPlusJeune = personne.getNom();
            }
            else{
                if (personne.getAge() < agePlusJeune){
                    agePlusJeune = personne.getAge();
                    nomPlusJeune = personne.getNom();
                }
            }
        }
        return nomPlusJeune;
    }

    public boolean sontACote(String pers1, String pers2){
        int indP1 = -1;
        int indP2 = -1;
        for (int i = 0; i < this.lesConvives.size(); i++) {
            if (this.lesConvives.get(i).getNom().equals(pers1)) {
                indP1 = i;
            }
            if (this.lesConvives.get(i).getNom().equals(pers2)) {
                indP2 = i;
            }
            
        }
        return true;
    }

}

