public class Executable {
    public static void main(String [] args){
        Train train = new Train();
        Wagon wagon1 = new Wagon(1);
        Wagon wagon2 = new Wagon(2);
        Wagon wagon3 = new Wagon(1);
        train.ajouterWagon(wagon1);
        train.ajouterWagon(wagon2);
        train.ajouterWagon(wagon3);
    }
}
