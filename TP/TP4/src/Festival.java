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

    public List<Concert> getConcerts() {
        return concerts;
    }

    public void reserver(Spectateur spectateur, Concert concert, int prix){
        

    }

    public int  nombreBilletConcert(Concert concert){
        return 0;
    }

    public int nombreConcert(){
        return 0;
    }
}
