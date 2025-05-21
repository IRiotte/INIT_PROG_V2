import java.util.*;

public class Achats {
    private Map<Produit, Integer> achats;

    public Achats() {
        this.achats = new HashMap<>();
    }

    public void ajouter(Produit produit, int qte){
        if (this.achats.keySet().contains(produit)){
            int val = this.achats.get(produit) + qte;
            this.achats.put(produit, val);
        }
        else {
            this.achats.put(produit, qte);
        }
    }

    
    public Double totalPrixNom(String nom){
        Double res = 0.0;
        for (Map.Entry<Produit, Integer> couple : this.achats.entrySet()){
            if (couple.getKey().equals(nom)){
                res += couple.getKey().getPrix() * couple.getValue();
            }
        }
        return res;
    }




    public String toString(){
        return this.achats.toString();
    }
}
