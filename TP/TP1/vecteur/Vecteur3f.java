public class Vecteur3f {
    private double premier;
    private double deuxieme;
    private double troisieme;

    public Vecteur3f(double premier, double deuxieme, double troisieme){
        this.premier = premier;
        this.deuxieme = deuxieme;
        this.troisieme = troisieme;
    }

    public double getPremier(){
        return this.premier;
    }

    public double getDeuxieme(){
        return this.deuxieme;
    }

    public double getTroisieme(){
        return this.troisieme;
    }

    public void modifier(double valeur, int numComposante){
        if (numComposante == 1) {
            this.premier = valeur;
        }
        if (numComposante == 2) {
            this.deuxieme = valeur;
        }
        if (numComposante == 3) {
            this.troisieme = valeur;
        }
    }

    public double norme(){
        return Math.sqrt((this.premier*this.premier) + (this.deuxieme*this.deuxieme) + (this.troisieme*this.troisieme));
    }

    @Override
    public String toString(){
        return "<" + this.premier + " " + this.deuxieme + " " + this.troisieme + "> De norme : " + this.norme();
    }
}