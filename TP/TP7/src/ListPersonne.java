import java.util.List;
import java.util.Collections;

public class ListPersonne {
    
    private List<Personne> liste;

    public ListPersonne(List<Personne> liste){
        this.liste = liste;
    }

    public void trier(){
        Collections.sort(this.liste);
        int ecartMin = 0;
        for (int i = 0; i < this.liste.size()-1; i++){
            /* Tester chaque personne côte à côte */
        }
    }

}
