public class ExecutableZoo {
    public static void main(String[] args){
        Zoo beauval = new Zoo("Beauval");
        Lion simba = new Lion("Simba", 55, false);
        Serpent python = new Serpent("Python", 10, true);
        beauval.ajouter(simba);
        beauval.ajouter(python);
        System.out.println(beauval);

        Animal lion = new Lion("Simba", 55, false);
        lion.emmettreUnSon();


    }
}
