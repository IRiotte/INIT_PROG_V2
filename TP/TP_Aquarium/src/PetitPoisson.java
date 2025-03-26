public class PetitPoisson extends ObjMarin{

    public Dessin getDessin(){
        Dessin dessin = new Dessin();
        dessin.ajouteChaine(posX, posY, "<><", "0x0000F0");
        return dessin;
    }

}