import java.util.Collections;

public class Fantome{
    private String nom;
    private int force;
    private int taille;

    public Fantome(String nom, int force, int taille){
        this.nom = nom;
        this.taille = taille;
        this.force = force;
    }

    public String getNom(){
        return this.nom;
    }

    public int getForce(){
        return this.force;
    }

    public int getTaille(){
        return this.taille;
    }

    @Override
    public String toString(){
        return this.nom + " - Force : " + this.force + " - Taille : " + this.taille;
    }

    @Override
    public boolean equals(Object objet){
        if (objet == null){return false;}
        if (!(objet instanceof Fantome)){return false;}
        Fantome tmp = (Fantome) objet;
        if (this.nom.equals(tmp.nom) && this.force == tmp.force && this.taille == tmp.taille){
            return true;
        }
        return false;
    }

    @Override
    public  int hashCode(){
        return this.nom.hashCode() + 31 * this.force + 2687 * taille;
    }


}
