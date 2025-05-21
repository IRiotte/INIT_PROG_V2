import java.util.*;

public class ExecNumber {
    
    public static void main(String[] args){

        List <Number > tableau = new ArrayList <>();
        tableau.add(5);
        tableau.add (6.);
        tableau.add(7.f);
        Number number = 8.5f;
        tableau.add(number);

        System.out.println(tableau);

        Number x = 5;
        Number y = 5.0;
        System.out.println(x.equals(y));
    }
}
