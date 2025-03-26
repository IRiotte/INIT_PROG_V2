public abstract class ObjMarin {
    protected int posX;
    protected int posY;
    protected int vitesseX;
    protected int vitesseY;

    protected void deplacer(){
        this.posX += vitesseX;
        this.posY += vitesseY;
    }

    protected abstract Dessin getDessin();
}
