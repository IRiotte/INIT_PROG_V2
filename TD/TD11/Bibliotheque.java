import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class Bibliotheque{
    
    public static void main(String[] args){
        List<Integer> test1 = Arrays.asList(1,8,6,7,-7,-2,-9);;
        System.out.println(sommeNulle(test1));

        List<Integer> test2 = Arrays.asList(1,8,6,7,-2,-9);
        System.out.println(sommeNulle(test2));

        List<Integer> test3 = Arrays.asList(4,-1,4,9,4,5,9,1,-3,-1);
        System.out.println(occurrences(test3));

        List<Integer> test4 = Arrays.asList(4,-1,4,9,4,5,9,1,-3,-1);
        List<Integer> test5 = Arrays.asList(-1,4,4,-3,5,4,9,-1,9,1);
        System.out.println(exactementMemesValeurs(test4, test5));

        List<Integer> test6 = Arrays.asList(1,6,2,-4,1,9,6);
        System.out.println(mediane(test6));

        List<Integer> test7 = Arrays.asList(1,6,2,-4,1,9);
        System.out.println(mediane(test7));
    }






    public static boolean sommeNulle(List<Integer> listeEntier){
        List<Integer> tmp = new ArrayList<>(listeEntier);
        Collections.sort(tmp);
        int i = 0;
        int j = tmp.size()-1;
        while (i < j){
            if ((tmp.get(j)+tmp.get(i)) == 0) {
                return true;
            }
            else if ((tmp.get(j)+tmp.get(i)) < 0) {
                ++i;
            }
            else {
                --j;
            }
        }
        return false;
    }


    public static List<Integer> occurrences(List<Integer> listeEntier){
        List<Integer> tmp = new ArrayList<>(listeEntier);
        Collections.sort(tmp);

        List<Integer> res = new ArrayList<>();

        Integer valPrec = null;
        for (Integer val : tmp){
            if (valPrec == null){
                res.add(val);
            }
            else if (val != valPrec){
                res.add(val);
            }
            valPrec = val;
        }
        return res;
    }


    public static boolean exactementMemesValeurs(List<Integer> liste1, List<Integer> liste2){
        List<Integer> tmp1 = new ArrayList<>(liste1);
        Collections.sort(tmp1);
        List<Integer> tmp2 = new ArrayList<>(liste2);
        Collections.sort(tmp2);

        if (tmp1.size() != tmp2.size()) {return false;}
        
        for (int i=0 ; i < tmp1.size() ; ++i){
            if (tmp1.get(i) != tmp2.get(i)) {return false;}
        }

        return true;
    }


    public static Integer mediane(List<Integer> liste){
        List<Integer> tmp = new ArrayList<>(liste);
        Collections.sort(tmp);

        if (tmp.size() % 2 == 1){
            return tmp.get(tmp.size() / 2);
        }
        else {
            return tmp.get(tmp.size() / 2);
        }
    }
}