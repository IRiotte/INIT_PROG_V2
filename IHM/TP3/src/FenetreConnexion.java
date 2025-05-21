import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.*;
import javafx.scene.text.Font;
import javafx.scene.text.FontWeight;
import javafx.scene.text.Text;
import javafx.stage.Stage;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.geometry.Pos;

 
 
public class FenetreConnexion extends GridPane{
    
    private Label tleLabel;
    private Label idLabel;
    private Label pswLabel;
    private TextField idField;
    private PasswordField pswField;
    private Button btnConnect;
    
    public FenetreConnexion(Button bouton){
        super();
        this.btnConnect = bouton;;
        init();
        this.getChildren().add(connexion());
    }
    
    public void init(){
        this.tleLabel = new Label("Entrez votre identifiant et votre mot de passe");        
        this.idLabel = new Label("Identifiant");
        this.pswLabel = new Label("Mot de passe");
        this.idField = new TextField();
        this.pswField = new PasswordField();
        
    }

    public VBox connexion() {
        VBox vbox = new VBox();
        vbox.setSpacing(10);
        vbox.setPadding(new Insets(20));
        HBox idHbox = idHBox();
        HBox pswHbox = pswHBox();
        vbox.getChildren().addAll(tleLabel, idHbox, pswHbox, btnConnect);
        vbox.setStyle("-fx-background-color: #98fb98;");
        return vbox;
    }

    public HBox idHBox(){
        HBox hbox = new HBox();
        hbox.setSpacing(10);
        hbox.setPadding(new Insets(10,0,10,0));
        hbox.getChildren().addAll(idLabel, idField);
        hbox.setAlignment(Pos.CENTER_LEFT);
        Region spacer = new Region();
        HBox.setHgrow(spacer, Priority.ALWAYS);
        hbox.getChildren().clear();
        hbox.getChildren().addAll(idLabel, spacer, idField);

        return hbox;
    }

    public HBox pswHBox(){
        HBox hbox = new HBox();
        hbox.setSpacing(10);
        hbox.setPadding(new Insets(10,0,10,0));
        Region spacer = new Region();
        HBox.setHgrow(spacer, Priority.ALWAYS);
        hbox.getChildren().addAll(pswLabel, spacer, pswField);
        return hbox;
    }
}
