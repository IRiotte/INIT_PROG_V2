import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.layout.Pane;
import javafx.stage.Stage;


 
public class AppliPlusieursFenetres extends Application {
    
    private Button btnConnect;
    private Scene scene;
 
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        launch(AppliPlusieursFenetres.class, args);
    }
    
    @Override
    public void init(){
        this.btnConnect = new Button("Connexion");        

        /*ControleBouton controleur = new ControleBouton(this);        
        this.btn1.setOnAction(controleur);
        this.btn2.setOnAction(controleur);*/
        
    }
    
    @Override
    public void start(Stage stage) {
        Pane root = new Fenetre3(this.btnConnect);
        this.scene = new Scene(root);
        stage.setScene(scene);
        stage.setTitle("Allo 45");
        stage.show();
    }
 
    /*public void afficheFenetre1(){
        Pane root = new Fenetre3(this.btn1);
        this.scene.setRoot(root);
    }*/
    
    /*public void afficheFenetre2(){
        Pane root = new Fenetre2(this.btn2);    
        this.scene.setRoot(root);
    }*/
}
