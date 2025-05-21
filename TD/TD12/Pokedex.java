import java.util.*;

public class Pokedex{
    private Map<Attaque, Set<String>> pokedex;

    public Pokedex(){
        this.pokedex = new HashMap<>();
    }

    public void ajouter(Attaque attaque, String nom){
        if (this.pokedex.containsKey(attaque)) {
            this.pokedex.get(attaque).add(nom);
        }
        else{
            this.pokedex.put(attaque, new HashSet<>());
            this.pokedex.get(attaque).add(nom);
        }
       
    }


    public boolean appartient(String nomPoke){
        for (Attaque attaque : this.pokedex.keySet()){
            if (this.pokedex.get(attaque).contains(nomPoke)){
                return true;
            }
        }
        return false;
    }


    



    
}