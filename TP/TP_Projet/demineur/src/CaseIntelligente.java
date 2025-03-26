import java.util.List;
import java.util.ArrayList;

public class CaseIntelligente extends Case {
    private List<Case> lesVoisines;
    

    public CaseIntelligente(){
        this.lesVoisines = new ArrayList<Case>();
    }

    public void ajouterVoisine(Case uneCase){
        this.lesVoisines.add(uneCase);
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
