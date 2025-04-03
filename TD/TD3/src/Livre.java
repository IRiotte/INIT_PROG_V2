public class Livre implements Comparable<Livre>{
    String titre;
    String auteur;
    int annee;
    double prix;
    int nbPage;

    public Livre(String titre, String auteur, int annee, double prix, int nbPage){
        
    }

    @Override
    public int compareTo(Livre livre){
        return this.annee - livre.annee;
    }
}
