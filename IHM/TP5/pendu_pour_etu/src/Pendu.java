import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.scene.text.Font;
import javafx.stage.Stage;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.layout.*;
import javafx.scene.paint.Color;
import javafx.scene.text.Text;
import javafx.scene.control.Tooltip;
import javafx.scene.control.TitledPane;
import javafx.scene.layout.Region;
import javafx.scene.text.TextAlignment;
import javafx.scene.control.Alert;
import javafx.scene.control.ButtonBar.ButtonData ;
import javafx.scene.control.ButtonType ;
import java.util.List;
import java.util.Arrays;
import java.io.File;
import java.util.ArrayList;



/**
 * Vue du jeu du pendu
 */
public class Pendu extends Application {
    private MotMystere modelePendu;

    private ArrayList<Image> lesImages;

    public List<String> niveaux;

    private ImageView dessin;

    private Text motCrypte;

    private ProgressBar pg;
    /**
     * le clavier qui sera géré par une classe à implémenter
     */
    private Clavier clavier;

    private Text leNiveau;
    /**
     * le chronomètre qui sera géré par une clasee à implémenter
     */
    private Chronometre chrono;

    //le panel Central qui pourra être modifié selon le mode (accueil ou jeu)
    private BorderPane panelCentral;

    
    private Button boutonParametres;
    private Button boutonMaison;
    private Button boutonInfo;
    private Button bJouer;

    /**
     * initialise les attributs (créer le modèle, charge les images, crée le chrono ...)
     */
    @Override
    public void init() {
        this.modelePendu = new MotMystere("/usr/share/dict/french", 3, 10, MotMystere.FACILE, 10);
        this.lesImages = new ArrayList<Image>();
        this.chargerImages("./img");
        this.niveaux = Arrays.asList("Facile", "Normal", "Difficile", "Hardcore ça mère");
        this.dessin = new ImageView(lesImages.get(0));
        this.motCrypte = new Text("test");
        this.pg = new ProgressBar();
        this.leNiveau = new Text();

        this.boutonParametres = new Button();
        ImageView imageView1 = new ImageView(new Image("file:./img/parametres.png"));
        imageView1.setFitWidth(50);
        imageView1.setFitHeight(50);
        this.boutonParametres.setGraphic(imageView1);

        this.boutonMaison = new Button();
        ImageView imageView2 = new ImageView(new Image("file:./img/home.png"));
        imageView2.setFitWidth(50);
        imageView2.setFitHeight(50);
        this.boutonMaison.setGraphic(imageView2);

        this.boutonInfo = new Button();
        ImageView imageView3 = new ImageView(new Image("file:./img/info.png"));
        imageView3.setFitWidth(50);
        imageView3.setFitHeight(50);
        this.boutonInfo.setGraphic(imageView3);

        this.bJouer = new Button("Jouer");
    }

    /**
     * @return  le graphe de scène de la vue à partir de methodes précédantes
     */
    private Scene laScene(){
        BorderPane fenetre = new BorderPane();
        fenetre.setTop(this.titre());
        fenetre.setCenter(this.panelCentral);
        return new Scene(fenetre, 800, 1000);
    }

    /**
     * @return le panel contenant le titre du jeu
     */
    private Pane titre(){          
        Pane banniere = new Pane();
        GridPane grid = new GridPane();
        Label titre = new Label("Jeu du Pendu");
        grid.add(titre, 1, 0);
        grid.add(boutonMaison, 4, 0);
        grid.add(boutonParametres, 5, 0);
        grid.add(boutonInfo, 6, 0);
        banniere.getChildren().addAll(grid);

        return banniere;
    }

    // /**
     // * @return le panel du chronomètre
     // */
    // private TitledPane leChrono(){
        // A implementer
        // TitledPane res = new TitledPane();
        // return res;
    // }

    // /**
     // * @return la fenêtre de jeu avec le mot crypté, l'image, la barre
     // *         de progression et le clavier
     // */
    // private Pane fenetreJeu(){
        // A implementer
        // Pane res = new Pane();
        // return res;
    // }

    // /**
     // * @return la fenêtre d'accueil sur laquelle on peut choisir les paramètres de jeu
     // */
    // private Pane fenetreAccueil(){
        // A implementer    
        // Pane res = new Pane();
        // return res;
    // }

    /**
     * charge les images à afficher en fonction des erreurs
     * @param repertoire répertoire où se trouvent les images
     */
    private void chargerImages(String repertoire){
        for (int i=0; i<this.modelePendu.getNbErreursMax()+1; i++){
            File file = new File(repertoire+"/pendu"+i+".png");
            System.out.println(file.toURI().toString());
            this.lesImages.add(new Image(file.toURI().toString()));
        }
    }

    public void modeAccueil(){
        BorderPane scene = new BorderPane();
    }
    
    public void modeJeu(){
        // A implementer
    }
    
    public void modeParametres(){
        // A implémenter
    }

    /** lance une partie */
    public void lancePartie(){
        // A implementer
    }

    /**
     * raffraichit l'affichage selon les données du modèle
     */
    public void majAffichage(){
        // A implementer
    }

    /**
     * accesseur du chronomètre (pour les controleur du jeu)
     * @return le chronomètre du jeu
     */
    public Chronometre getChrono(){
        // A implémenter
        return null; // A enlever
    }

    public Alert popUpPartieEnCours(){
        Alert alert = new Alert(Alert.AlertType.CONFIRMATION,"La partie est en cours!\n Etes-vous sûr de l'interrompre ?", ButtonType.YES, ButtonType.NO);
        alert.setTitle("Attention");
        return alert;
    }
        
    public Alert popUpReglesDuJeu(){
        // A implementer
        Alert alert = new Alert(Alert.AlertType.INFORMATION);
        return alert;
    }
    
    public Alert popUpMessageGagne(){
        // A implementer
        Alert alert = new Alert(Alert.AlertType.INFORMATION);        
        return alert;
    }
    
    public Alert popUpMessagePerdu(){
        // A implementer    
        Alert alert = new Alert(Alert.AlertType.INFORMATION);
        return alert;
    }

    /**
     * créer le graphe de scène et lance le jeu
     * @param stage la fenêtre principale
     */
    @Override
    public void start(Stage stage) {
        stage.setTitle("IUTEAM'S - La plateforme de jeux de l'IUTO");
        stage.setScene(this.laScene());
        this.modeAccueil();
        stage.show();
    }

    /**
     * Programme principal
     * @param args inutilisé
     */
    public static void main(String[] args) {
        launch(args);
    }    
}
