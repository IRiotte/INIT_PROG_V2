import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

public class Bibliotheque {

    public static List<Integer> compressionListe(List<Integer> liste){
        List<Integer> tmp = new ArrayList<>(liste);
        Collections.sort(tmp);
        List<Integer> res = new ArrayList<>();
        int cpt = 0;
        for (int i = 0 ; i < tmp.size()-1 ; i++){
            if (tmp.get(i).equals(tmp.get(i+1))){
                ++cpt;
            }
            else {
                ++cpt;
                res.add(cpt);
                res.add(tmp.get(i));
            }
        }
        return res;
    }

    public static boolean enCommun(List<Integer> liste1, List<Integer> liste2){

        for (Integer entier1 : liste1){
            for (Integer entier2 : liste2){
                if (entier1 == entier2){
                    return true;
                }
            }
        }
        return false;
    }


    public static List<Integer> intersection(List<Integer> liste1, List<Integer> liste2){
        List<Integer> listeRes = new ArrayList<>();
        
        for (Integer entier1 : liste1){
            for (Integer entier2 : liste2){
                if (entier1 == entier2){
                    listeRes.add(entier1);
                    break;
                }
            }
        }
        return listeRes;
    }

    
}
