public class Personne implements Comparable<Personne>{
    
    private String nom;
    private int age;

    public Personne(String nom, int age){
        this.nom = nom;
        this.age = age;
    }

    
    public String getNom() {
        return this.nom;
    }

    public int getAge() {
        return this.age;
    }

    @Override
    public int compareTo(Personne personne){
        return this.age - personne.age;
    }

}
