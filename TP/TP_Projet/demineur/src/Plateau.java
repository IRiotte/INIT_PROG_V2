import java.util.List;
import java.util.ArrayList;
import java.util.Random;

public class Plateau{

    private int nbLignes;
    private int nbColonnes;
    private int pourcentageDeBombes;
    private int nbBombes;
    private List<CaseIntelligente> lePlateau;


    public Plateau(int nbLignes, int nbColonnes, int pourcentage){
        this.nbLignes = nbLignes;
        this.nbColonnes = nbColonnes;
        this.pourcentageDeBombes = pourcentage;
        this.nbBombes = 0;
        this.lePlateau = new ArrayList<CaseIntelligente>();
    }

    private void creerLesCasesVides(){
        for (int i = 0; i < this.getNbLignes(); i++){
            for (int j = 0; j < this.getNbColonnes(); j++){
                CaseIntelligente uneCase = null;
                this.lePlateau.add(uneCase);
            }
        }
    }

    private void rendLesCasesIntelligentes(){
        for (int i = 0; i < this.getNbLignes(); i++){
            for (int j = 0; j < this.getNbColonnes(); j++){
                CaseIntelligente uneCase = new CaseIntelligente();
                this.lePlateau.set(i*this.getNbColonnes()+j, uneCase);
            }
        }
    }


    protected void poseDesBombesAleatoirement(){
        Random generateur = new Random();
        for (int x = 0; x < this.getNbLignes(); x++){
            for (int y = 0; y < this.getNbColonnes(); y++){
                if (generateur.nextInt(100)+1 < this.pourcentageDeBombes){
                    this.poseBombe(x, y);
                    this.nbBombes = this.nbBombes + 1;
                }
            }
        }
    }

    public int getNbLignes(){
        return this.nbLignes;
    }

    public int getNbColonnes(){
        return this.nbColonnes;
    }

    public int getNbTotalBombes(){
        return this.nbBombes;
    }

    public CaseIntelligente getCase(int numLigne, int numColonne){
        return this.lePlateau.get(numLigne*this.getNbColonnes()+numColonne);
    }

    public int getNbCasesMarquees(){
        int nbMarquees = 0;
        for (int i = 0; i < this.getNbLignes(); i++){
            for (int j = 0; j < this.getNbColonnes(); j++){
                if (this.getCase(i, j).estMarquee()){
                    nbMarquees++;
                }
            }
        }
        return nbMarquees;
    }

    public void poseBombe(int x, int y){
        this.getCase(x, y).poseBombe();
        for (int i = x-1; i <= x+1; i++){
            for (int j = y-1; j <= y+1; j++){
                if (i >= 0 && i < this.getNbLignes() && j >= 0 && j < this.getNbColonnes()){
                    if (this.getCase(i, j) != this.getCase(x, y)){
                        this.getCase(i, j).ajouterVoisine(this.getCase(x, y));
                    }
                }
            }
        }
    }

    public void reset(){
        for (int i = 0; i < this.getNbLignes(); i++){
            for (int j = 0; j < this.getNbColonnes(); j++){
                this.getCase(i, j).reset();
            }
        }
        this.nbBombes = 0;
    }   

}
