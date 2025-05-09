import java.util.List;
import java.util.ArrayList;

public class Wagon {
    
    private List<Siege> sieges;
    private int classe;


    public Wagon(int classe){
        this.classe = classe;
        this.sieges = new ArrayList<>();
    }

    public List<Siege> getSiegesLibres(String date){
        List<Siege> siegesLibres = new ArrayList<>();
        for (Siege siege : this.sieges){
            if (siege.estLibre(date)){
                siegesLibres.add(siege);
            }
        }
        return siegesLibres;
    }

    public int getClasse(){
        return this.classe;
    }

    public List<Siege> getSieges(){
        return this.sieges;
    }
}
