import java.util.List;
import java.util.ArrayList;

public class Concert {
    private String nomConcert;
    private String nomGroupe;
    private List<Billet> billets;

    
    public Concert(String nomConcert, String nomGroupe) {
        this.nomConcert = nomConcert;
        this.nomGroupe = nomGroupe;
        this.billets = new ArrayList<>();
    }

    public String getNomConcert(){
        return this.nomConcert;
    }

    public String getNomGroupe(){
        return this.nomGroupe;
    }

    public int getNbrBillets(){
        return billets.size();
    }

    public void ajouterBillet(Billet billet){
        billets.add(billet);
    }
    
}
