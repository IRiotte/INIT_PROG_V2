import java.util.*;

public class Pokedex{
    private Map<Attaque, Set<String>> pokedex;

    public Pokedex(){
        this.pokedex = new HashMap<>();
    }

    public void ajouter(Attaque attaque, String nom){
        this.pokedex.get(attaque).add(nom);
    }

    
}