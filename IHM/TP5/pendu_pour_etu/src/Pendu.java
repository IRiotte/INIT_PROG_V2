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
import javafx.scene.text.TextAlignment;
import javafx.scene.control.ButtonBar.ButtonData ;

import java.util.List;
import java.util.Arrays;
import java.io.File;
import java.time.chrono.ThaiBuddhistDate;
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

    private Clavier clavier;

    private Text leNiveau;
    /**
     * le chronomètre qui sera géré par une clasee à implémenter
     */
    private Chronometre chrono;

    //le panel Central qui pourra être modifié selon le mode (accueil ou jeu)
    private BorderPane panelCentral;

    private BorderPane fenetre;

    
    private Button boutonParametres;
    private Button boutonMaison;
    private Button boutonInfo;
    private Button bJouer;
    private Button btnNouvMot;

    /**
     * initialise les attributs (créer le modèle, charge les images, crée le chrono ...)
     * 
     * "/usr/share/dict/french"
     */
    @Override
    public void init() {
        //this.modelePendu = new MotMystere("data/french.txt", 2, 7, MotMystere.FACILE, 10);
        this.modelePendu = new MotMystere("manger", MotMystere.FACILE, 10);
        this.lesImages = new ArrayList<Image>();
        this.chargerImages("./img");
        this.niveaux = Arrays.asList("Facile", "Normal", "Difficile", "Hardcore");
        this.dessin = new ImageView(lesImages.get(0));
        this.motCrypte = new Text(modelePendu.getMotCrypte());
        this.pg = new ProgressBar(0.2);

        this.leNiveau = new Text("Niveau " + niveaux.get(modelePendu.getNiveau()));

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
        this.boutonMaison.setOnAction(new RetourAccueil(modelePendu, this));

        this.boutonInfo = new Button();
        ImageView imageView3 = new ImageView(new Image("file:./img/info.png"));
        imageView3.setFitWidth(50);
        imageView3.setFitHeight(50);
        this.boutonInfo.setGraphic(imageView3);

        this.bJouer = new Button("Lancer une partie");
        this.bJouer.setOnAction(new ControleurLancerPartie(modelePendu, this));

        this.btnNouvMot = new Button("Nouveau mot");


        this.clavier = new Clavier("ABCDEFGHIJKLMNOPQRSTUVWXYZ", new ControleurLettres(modelePendu, this));

        this.chrono = new Chronometre();
    }

    /**
     * @return  le graphe de scène de la vue à partir de methodes précédantes
     */
    private Scene laScene(){
        this.fenetre = new BorderPane();
        fenetre.setTop(this.titre());
        fenetre.setCenter(this.panelCentral);
        return new Scene(fenetre, 800, 1000);
    }

    /**
     * @return le panel contenant le titre du jeu
     */
    private Pane titre(){          
        BorderPane panel = new BorderPane();
        HBox hboxTtr = new HBox();
        Label titre = new Label("Jeu du Pendu");
        titre.setFont(new Font(50));
        hboxTtr.getChildren().add(titre);
        hboxTtr.setPadding(new Insets(15,15,15,15));
        HBox hboxBtn = new HBox();
        hboxBtn.getChildren().addAll(boutonMaison,boutonParametres, boutonInfo);
        hboxBtn.setPadding(new Insets(15,15,15,15));
        panel.setLeft(hboxTtr);
        panel.setRight(hboxBtn);
        panel.setBackground(new Background(new BackgroundFill(Color.LAVENDER, CornerRadii.EMPTY, Insets.EMPTY)));
        return panel;
    }

    // /**
     // * @return le panel du chronomètre
     // */
    private TitledPane leChrono(){
        TitledPane res = new TitledPane("Chronometre", this.chrono);
        res.setCollapsible(false);
        return res;
    }

    // /**
     // * @return la fenêtre de jeu avec le mot crypté, l'image, la barre
     // *         de progression et le clavier
     // */
    private Pane fenetreJeu(){
        VBox vboxMot = new VBox();
        vboxMot.setAlignment(Pos.TOP_CENTER);
        vboxMot.setPadding(new Insets(15,15,15,15));
        vboxMot.getChildren().addAll(this.motCrypte, this.dessin, this.pg, this.clavier);
        vboxMot.setSpacing(15);
        return vboxMot;
    }

    // /**
     // * @return la fenêtre d'accueil sur laquelle on peut choisir les paramètres de jeu
     // */
    private BorderPane fenetreAccueil(){  
        BorderPane panelAcc = new BorderPane();
        VBox vboxScn = new VBox();
        vboxScn.setPadding(new Insets(15,15,15,15));
        ToggleGroup groupNiveaux = new ToggleGroup();
        VBox vboxRadios = new VBox();
        vboxRadios.setSpacing(5);
        for (String niveau : this.niveaux) {
            RadioButton rb = new RadioButton(niveau);
            rb.setToggleGroup(groupNiveaux);
            vboxRadios.getChildren().add(rb);
        }
        TitledPane titledPaneNiveaux = new TitledPane("Niveau de difficulté", vboxRadios);
        titledPaneNiveaux.setCollapsible(false);
        titledPaneNiveaux.setPadding(new Insets(15, 0, 15, 0));
        vboxScn.getChildren().addAll(bJouer, titledPaneNiveaux);
        panelAcc.setTop(vboxScn);
        return panelAcc;
    }

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
        this.panelCentral = this.fenetreAccueil();
        this.fenetre.setCenter(panelCentral);
    }
    
    public void modeJeu(){
        BorderPane panelJeu = new BorderPane();


        VBox vboxMenu = new VBox();
        vboxMenu.setPadding(new Insets(15));
        vboxMenu.getChildren().addAll(this.leNiveau, this.leChrono(), this.btnNouvMot);
        vboxMenu.setSpacing(15);
        vboxMenu.setPrefWidth(fenetre.getWidth()*0.33);

        panelJeu.setCenter(this.fenetreJeu());
        panelJeu.setRight(vboxMenu);
        this.panelCentral = panelJeu;
        this.fenetre.setCenter(panelCentral);
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
        Alert alert = new Alert(Alert.AlertType.CONFIRMATION,"Une partie est déjà en cours !\n Etes-vous sûr de vouloir l'interrompre ?", ButtonType.YES, ButtonType.NO);
        alert.setTitle("Attention");
        return alert;
    }

    public Alert popUpLancePartie(){
        Alert alert = new Alert(Alert.AlertType.CONFIRMATION,"Lancement de partie\n Etes-vous sûr de lancer une partie ?", ButtonType.YES, ButtonType.NO);
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
        //this.modeAccueil();
        this.modeJeu();
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
