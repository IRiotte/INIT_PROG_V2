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

 
 
public class Fenetre3 extends GridPane{
    
    private Label tleLabel;
    private Label idLabel;
    private Label pswLabel;
    private TextField field1;
    private PasswordField field2;
    private Button btnConnect;
    
    public Fenetre3(Button bouton){
        super();
        this.btnConnect = bouton;
        init();
        start();
    }
    
    public void init(){
        this.tleLabel = new Label("Entrez votre identifiant et votre mot de passe");        
        this.idLabel = new Label("Identifiant");
        this.pswLabel = new Label("Mot de passe");
        this.field1 = new TextField();
        this.field2 = new PasswordField();
        
    }

    public void start() {
        VBox vbox = new VBox();
        vbox.setSpacing(10);
        vbox.setPadding(new Insets(20));
        vbox.getChildren().add(new Text("Tables de multiplication"));
        vbox.getChildren().addAll(tleLabel, idLabel, pswLabel, field1, field2, btnConnect);
        vbox.setStyle("-fx-background-color: #98fb98;");
    }
}
