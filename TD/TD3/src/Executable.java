
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Executable {
    public static void main(String[] args){
        List<Integer> liste1 = Arrays.asList(1,5,3,12);
        List<Integer> liste2 = Arrays.asList(4,1,3,12);

        System.out.println(Bibliotheque.intersection(liste1, liste2));


        List<Integer> liste3 = Arrays.asList(1,5,3,12);
        List<Integer> liste4 = Arrays.asList(4,1,1,3,12);
        System.out.println(Bibliotheque.intersection(liste3, liste4));
    }
}
