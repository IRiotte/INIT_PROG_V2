import java.util.List;
import java.util.ArrayList;

public class Zoo {
    private String nom;
    private List<Animal> lesAnimaux;

    public Zoo(String nom){
        this.lesAnimaux = new ArrayList<>();
        this.nom = nom;
    }

    public boolean ajouter(Animal animal){
        if (this.lesAnimaux.contains(animal)){return false;}

        this.lesAnimaux.add(animal);
        return true;
    }

    @Override
    public String toString(){
        return "Zoo" + this.nom + " contient " + this.lesAnimaux;
    }
}
