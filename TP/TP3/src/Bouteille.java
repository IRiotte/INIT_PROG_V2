public class Bouteille {
    private String nom;
    private int annee;
    private String region;


    public Bouteille(String region, String nom, int annee){
        this.region = region;
        this.nom = nom;
        this.annee = annee;
    }


    public int getMillesime(){
        return this.annee;
    }

    public String getRegion(){
        return this.region;
    }

    public String getAppellation(){
        return this.nom;
    }

    @Override
    public boolean equals(Object objet){
        if (objet == null) {return false;}
        if (objet == this) {return true;}
        if (! (objet instanceof Bouteille)) {return false;}
    
        Bouteille tmp = (Bouteille) objet;
        return this.region == tmp.region 
        && this.nom == tmp.nom 
        && this.annee == tmp.annee;
    }

    


}
