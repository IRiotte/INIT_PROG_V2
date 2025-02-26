public class Billet {
    private int prix;
    private Concert concert;
    private Spectateur spectateur;


    public Billet(Concert concert, Spectateur spectateur) {
        this.concert = concert;
        this.spectateur = spectateur;
    }



    public Concert getConcert() {
        return concert;
    }
    public Spectateur getSpectateur() {
        return spectateur;
    }
}
