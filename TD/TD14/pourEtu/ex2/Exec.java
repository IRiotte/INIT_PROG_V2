import java.util.*;

public class Exec {
    
    
    public static void main(String[] args) {
        List<Integer> l = new ArrayList<>();
        l.add(5);
        l.add(4);
        Iterator<Integer> iterateur = l.iterator();

        while (iterateur.hasNext()){
            System.out.println(iterateur.next());
        }

        List<Integer> l2 = new ArrayList<>();
        l2.add(3);
        l2.add(6);
        l2.add(3);
        l2.add(2);
        l2.add(1);
        l2.add(-3);
        l2.add(2);

        System.out.println(Iterateur.mystere0(l2));
        System.out.println(Iterateur.mystere1(l2, 3));
        System.out.println(Iterateur.mystere1(l2, 12));


        
    }
}
