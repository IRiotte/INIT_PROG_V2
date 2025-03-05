import java.util.List;
import java.util.ArrayList;

public class Festival {
    private String nom;
    private String adresse;
    private List<Concert> concerts;

    
    public Festival(String nom, String adresse) {
        this.nom = nom;
        this.adresse = adresse;
        this.concerts = new ArrayList<>();
    }

    public Festival(String nom) {
        this.nom = nom;
        this.nom = "";
        this.concerts = new ArrayList<>();
    }


    public List<Concert> getConcerts() {
        return concerts;
    }

    public void ajouterConcert(Concert concert){
        concerts.add(concert);
    }

    public void reserver(Spectateur spectateur, Concert concert, int prix){
        Billet billet = new Billet(concert, spectateur, prix);
        concert.ajouterBillet(billet);
    }

    public int  nombreBilletConcert(Concert concert){
        return concert.getNbrBillets();
    }

    public int nombreConcert(){
        return concerts.size();
    }

    
}
