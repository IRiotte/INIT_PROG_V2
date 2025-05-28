import java.util.*;

public class Bibliotheque {

    public static <T> void afficheTous(Iterable<T> iterable) {
        for (T element : iterable) {
            System.out.println(element);
        }

        Iterator<T> iterator = iterable.iterator();

        while (iterator.hasNext()) {
            System.out.println(iterator.next());
        }
    }





    public static void main(String[] args){
        List<Integer> l = new ArrayList<>();
        l.add(4);
        l.add(3);
        l.add(5);
        l.add(8);
        afficheTous(l);
    }


    public T getMin(Iterator<T>){
        Iterator <T > iterateur = coll . iterator () ;
T candidate = iterateur . next () ;
while ( iterateur . hasNext () ) {
T next = iterateur . next () ;
i f ( next . compareTo ( candidate ) < 0)
candidate = next ;
}
return candidate ;
}
    }

    
}
