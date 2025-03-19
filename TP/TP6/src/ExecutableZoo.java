public class ExecutableZoo {
    public static void main(String[] args){
        Zoo beauval = new Zoo("Beauval");
        Lion simba = new Lion("Simba", 55, false);
        beauval.ajouter(simba);
        System.out.println(beauval);
    }
}
