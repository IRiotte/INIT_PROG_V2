import java.util.List;
import java.util.ArrayList;

public class Maison {
    private String nom;
    private List<Sorcier> eleves;

    public Maison(String nom) {
        this.nom = nom;
        this.eleves = new ArrayList<>();
    }

    public List<Sorcier> getEleves(){
        return this.eleves;
    }

    public boolean ajouter(Sorcier sorcier) {
        return this.eleves.add(sorcier);
    }

    public int nombreEleves() {
        return this.eleves.size();
    }

    public boolean contientCourageux() {
        for (Sorcier sorcier : eleves) {
            if (sorcier.estCourageux()) {
                return true;
            }
        }
        return false;
    }

    public Sorcier leMoinsCourageux() {
        Integer courageMin = null;
        Sorcier leMoinsCourageux = null;
        for (Sorcier sorcier : this.eleves){
            if (leMoinsCourageux == null || sorcier.getCourage() < courageMin){
                leMoinsCourageux = sorcier;
                courageMin = sorcier.getCourage();
            }
        }
        return leMoinsCourageux;
    }


    public Sorcier lePlusSage() {
        Integer sagesseMax = null;
        Sorcier lePlusSage = null;
        for (Sorcier sorcier : this.eleves){
            if (lePlusSage == null || sorcier.getSagesse() > sagesseMax){
                lePlusSage = sorcier;
                sagesseMax = sorcier.getSagesse();
            }
        }
        return lePlusSage;
    }

}
