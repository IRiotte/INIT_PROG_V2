import java.util.List;
import java.util.ArrayList;

public class CaseIntelligente {
    private List<Case> lesVoisines;
    

    public CaseIntelligente(){
        this.lesVoisines = new ArrayList<Case>();
    }

    public void ajouterVoisine(Case c){
        this.lesVoisines.add(c);
    }

    public int nombreBombesVoisines(){
        int nbBombe = 0;
        for(Case c : this.lesVoisines){
            if(c.contientUneBombe()){
                nbBombe++;
            }
        }
        return nbBombe;
    }

    @Override
    public String toString(){
        return "Nombre de bombes voisines : " + this.nombreBombesVoisines();
    }
}
