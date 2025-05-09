import java.util.*;

public class MaisonHantee implements Collections{
    private String nom;
    private Set<Fantome> fantomes;

    public MaisonHantee(String nom){
        this.nom = nom;
        this.fantomes = new HashSet<>();
    }

    public String getNom(){
        return this.nom;
    }

    public String fantomeLePlusFort(){
        Fantome res = null;
        for (Fantome fantome : this.fantomes){
            if (res == null){
                res = fantome;
            }
            else if (fantome.getForce() > res.getForce()){
                res = fantome;
            }
        }
        return res.getNom();
    }

    public Set<Fantome> fantomeDeForceDonnee(int force){
        Set<Fantome> res = new HashSet<>();
        for (Fantome fantome : this.fantomes){
            if (fantome.getForce() == force){
                res.add(fantome);
            }
        }
        return res;
    }

    public void ajouter(Fantome fantome){
        this.fantomes.add(fantome);
    }


    
}
