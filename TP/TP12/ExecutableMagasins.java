public class ExecutableMagasins{
    public static void main(String[] args){
        /*Magasin fleurus = new Magasin("Fleurus", true, false);
        Ville trainou = new Ville("Trainou");
        Magasin beauMagasin = new Magasin("Fleurus", true, true);
        Magasin venir = new Magasin("Fleurus", false, false);
        Magasin magnifique = new Magasin("Fleurus", false, true);
        Magasin bauchamp = new Magasin("Fleurus", true, false);
        trainou.ajouteMagasin(beauMagasin);
        trainou.ajouteMagasin(venir);
        trainou.ajouteMagasin(magnifique);
        rainou.ajouteMagasin(bauchamp);*/

        //System.out.println(trainou.toString());

        //trainou.ouvertsLeLundi();


        Produit salade1 = new Produit("Salade", 1.5);
        Produit brocolis = new Produit("Brocolis", 2.75);
        System.out.println(salade1);
    

        Achats achats = new Achats ();
        
        achats.ajouter(brocolis, 4);
        achats.ajouter(salade1, 2);

        System.out.println(achats);
        }
}