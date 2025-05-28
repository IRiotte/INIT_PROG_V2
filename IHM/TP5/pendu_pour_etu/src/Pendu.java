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

import javax.sound.sampled.Control;

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
     * "data/french.txt"
     */
    @Override
    public void init() {
        this.modelePendu = new MotMystere("/usr/share/dict/french", 3, 7, MotMystere.FACILE, 10);
        this.modelePendu.setMotATrouver("n");
        this.lesImages = new ArrayList<Image>();
        this.chargerImages("./img");
        this.niveaux = Arrays.asList("Facile", "Moyen", "Difficile", "Hardcore");
        this.dessin = new ImageView(lesImages.get(0));
        this.motCrypte = new Text(modelePendu.getMotCrypte());
        this.pg = new ProgressBar(0.0);

        this.leNiveau = new Text();
        this.leNiveau.setFont(new Font(30));

        this.boutonParametres = new Button();
        ImageView imageView1 = new ImageView(new Image("file:./img/parametres.png"));
        imageView1.setFitWidth(50);
        imageView1.setFitHeight(50);
        this.boutonParametres.setGraphic(imageView1);
        this.boutonInfo.setOnAction(new ControleurParametre(modelePendu, this));

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
        this.boutonInfo.setOnAction(new ControleurInfos(this));

        this.bJouer = new Button("Lancer une partie");
        this.bJouer.setOnAction(new ControleurLancerPartie(modelePendu, this));

        this.btnNouvMot = new Button("Nouveau mot");
        this.btnNouvMot.setOnAction(new ControleurLancerPartie(modelePendu, this));


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
            rb.setOnAction(new ControleurNiveau(modelePendu));
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
        this.boutonMaison.setDisable(true);
        this.modelePendu.setMotATrouver("n");
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
        /**
         * a faire plus tard (ou pas)
         */
    }

    /** lance une partie */
    public void lancePartie(){
        
        //this.chrono.startChrono();
        this.modelePendu.setMotATrouver();
        this.motCrypte.setText(modelePendu.getMotCrypte());
        this.dessin.setImage(lesImages.get(0));
        this.boutonMaison.setDisable(false);
        this.clavier.desactiveTouches(this.modelePendu.getLettresEssayees());
        switch (this.modelePendu.getNiveau()) {
            case 0:
                this.leNiveau.setText("Niveau Facile");
                break;
            case 1:
                this.leNiveau.setText("Niveau Moyen");
                break;
            case 2:
                this.leNiveau.setText("Niveau Difficile");
                break;
            case 3:
                this.leNiveau.setText("Niveau Hardcore");
                break;
        }
        double nbLettresRest = modelePendu.getNbLettresRestantes();
        double nbLettre = modelePendu.getMotATrouve().length();
        this.pg.setProgress(1.0 - nbLettresRest / nbLettre);
        this.modeJeu();

        System.out.println(modelePendu);
        
    }

    /**
     * raffraichit l'affichage selon les données du modèle
     */
    public void majAffichage(){
        this.motCrypte.setText(modelePendu.getMotCrypte());
        this.dessin.setImage(lesImages.get(10 - modelePendu.getNbErreursRestants()));
        System.out.println(modelePendu.getMotATrouve().length());
        System.out.println(modelePendu.getNbLettresRestantes());

        double nbLettresRest = modelePendu.getNbLettresRestantes();
        double nbLettre = modelePendu.getMotATrouve().length();
        this.pg.setProgress(1.0 - nbLettresRest / nbLettre);
        System.out.println(modelePendu);
        if (modelePendu.gagne()) {
            clavier.desactiveToutesLesTouches();
            this.chrono.stop();
            this.popUpMessageGagne().showAndWait();
        } 
        else if (modelePendu.perdu()) {
            clavier.desactiveToutesLesTouches();
            this.chrono.stop();
            this.popUpMessagePerdu().showAndWait();
        }


        
    }

    /**
     * accesseur du chronomètre (pour les controleur du jeu)
     * @return le chronomètre du jeu
     */
    public Chronometre getChrono(){
        return this.chrono;
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
        Alert alert = new Alert(Alert.AlertType.INFORMATION, "Regles du jeu : \n Séléctionner une lettre pour tester si elle appartient au mot à trouver. \n si oui, alors la lettre s'affiche dans le mot. \n si non, alors vous perdez une tentive et le dessin progresse. \n la partie se termine lorsque vous avez complété le mot ou que vous n'avez plus de tentative restante.", ButtonType.OK);  
        return alert;
    }
    
    public Alert popUpMessageGagne(){
        Alert alert = new Alert(Alert.AlertType.INFORMATION, "Victoire !\n Vous avez gagnez la partie", ButtonType.OK);    
        return alert;
    }
    
    public Alert popUpMessagePerdu(){  
        Alert alert = new Alert(Alert.AlertType.INFORMATION, "Défaite !\n Vous avez perdu la partie. \n Le mot à trouver était : " + modelePendu.getMotATrouve(), ButtonType.OK);
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
