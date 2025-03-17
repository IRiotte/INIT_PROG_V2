import java.util.*;

public class WeekEnd{
    private String dateDuWeekEnd;
    private List<Personne> participants;
    private List<Depense> lesDepenses;

    public WeekEnd(String date){
        this.dateDuWeekEnd = date;
        this.participants = new ArrayList<>();
        this.lesDepenses = new ArrayList<>();
    }

    public void ajouteParticipant(String prenom, int age){
        this.participants.add(new Personne(prenom, age));
    }

    public void ajouteDepense(double montant, String produit, String prenom, int age){
        boolean trouve = false;
        for (Personne personne : this.participants){
            if (personne.getNom().equals(prenom)){
                this.lesDepenses.add(new Depense(personne, montant, produit));
            trouve = true;
            }
            break;
        }
        if (! trouve){
            Personne payeur = new Personne(prenom, age);
            this.lesDepenses.add(new Depense(payeur, montant, produit));
        }
    }


    public double totalDepense(Personne personne){
        double total = 0;
        for (Depense depense : lesDepenses){
            if (depense.getPayeur().equals(personne)){
                total += depense.getMontant();
            }
        }
        return total;
    }


    public double totalDepense(){
        double total = 0;
        for (Depense depense : this.lesDepenses){
           total += depense.getMontant();
        }
        return total;
        }

    public double totalDepense(String produit){
        double total = 0;
        for (Depense depense : this.lesDepenses){
            if (depense.getProduit().equals(produit)){
                total += depense.getMontant();
            }
        }
        return total;
    }

    public double avoirPersonne(Personne personne){
        double totalDepense = this.totalDepense();
        double totalDepensePersonne = this.totalDepense(personne);
        double moyenneTotal = 0;
        if (!(this.lesDepenses.size() == 0)){
            moyenneTotal = totalDepense / this.participants.size();
        }
        double avoir = totalDepensePersonne - moyenneTotal;
        return avoir;
    }
}