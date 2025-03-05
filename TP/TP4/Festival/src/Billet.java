public class Billet {
    private int prix;
    private Concert concert;
    private Spectateur spectateur;


    public Billet(Concert concert, Spectateur spectateur, int prix) {
        this.concert = concert;
        this.spectateur = spectateur;
        this.prix = prix;
    }


    public Concert getConcert() {
        return concert;
    }
    public Spectateur getSpectateur() {
        return spectateur;
    }
    public int getPrix(){
        return this.prix;
    }



}
