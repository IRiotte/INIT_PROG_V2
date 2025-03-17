public class Personne{
    private String nom;
    private int age;

    public Personne(String nom, int age){
        this.nom = nom;
        this.age = age;
    }

    public String getNom(){
        return this.nom;
    }


    @Override
    public boolean equals(Object objet){
        if (objet == null) {return false;}
        if (objet == this) {return true;}
        if (! (objet instanceof Personne)) {return false;}
    
        Personne tmp = (Personne) objet;
        return this.nom.equals(tmp.nom) && this.age == tmp.age;
    }
}