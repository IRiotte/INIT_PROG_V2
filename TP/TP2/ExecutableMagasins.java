public class ExecutableMagasins{
    public static void main(String[] args){
        Magasin fleurus = new Magasin("Fleurus", true, false);
        Ville trainou = new Ville("Trainou");
        Magasin beauMagasin = new Magasin("Fleurus", true, true);
        Magasin venir = new Magasin("Fleurus", false, false);
        Magasin magnifique = new Magasin("Fleurus", false, true);
        Magasin bauchamp = new Magasin("Fleurus", true, false);
        trainou.ajouteMagasin(beauMagasin);
        trainou.ajouteMagasin(venir);
        trainou.ajouteMagasin(magnifique);
        trainou.ajouteMagasin(bauchamp);

        System.out.println(trainou.toString());

        //trainou.ouvertsLeLundi();


    }
}