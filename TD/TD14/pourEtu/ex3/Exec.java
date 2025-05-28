public class Exec {
    
    public static void main(String[] args){

        IterateurMystere iterateur = new IterateurMystere("quoicoubeh");
        while (iterateur.hasNext()){
            System.out.println(iterateur.next());
        }

        Mystere mystere = new Mystere("quoicoubeh");
        //while (mystere.hasNext()){
        //    System.out.println(mystere.next());
        //}
    }
}
