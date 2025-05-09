import javafx.application.Application;
import javafx.application.Platform;
// import javafx.beans.binding.Bindings;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.event.ActionEvent;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.control.RadioButton;
import javafx.scene.control.TextArea;
import javafx.scene.control.ToggleGroup;
import javafx.scene.input.*;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.scene.layout.Pane;
import javafx.stage.Stage;
import javafx.scene.image.ImageView;

public class AppliConverter extends Application {

    private TextField textField1 ;
    private TextField textField2 ;
    private Label resultatLabel ;
    private Resultat resultat;
    private ToggleGroup operationGroup;
    private Button calcButton, eraseButton;
    private Button addButton, subButton, multButton, divButton, selectedButton;
    private TextArea savedOp;

    @Override
    public void init(){
        // Initialisation des objects qui ne sont pas dans la scène
        // cad des éléments non graphiques
        this.resultat = new Resultat();

        this.textField1 = new TextField();
        this.textField2 = new TextField();

        this.addButton = new Button("+");
        this.addButton.setPadding(new Insets(10,25,10,25));

        this.subButton = new Button("-");
        this.subButton.setPadding(new Insets(10,25,10,25));
        
    }

    @Override
    public void start(Stage stage) throws Exception{
        // Construction du graphe de scène
        VBox root = new VBox();

        this.ajouteChamp(root);
        this.ajouteBoutons(root);
        
        Scene scene = new Scene(root);
        stage.setTitle("Calculette");
        stage.setScene(scene);
        stage.show();
    }

    public void effaceTF(){
        this.textField1.setText("");
        this.textField2.setText("");
    }
    
    public double getValueChamp2() throws NumberFormatException{
        return Double.parseDouble(textField1.getText());
    }

    public double getValueChamp1() throws NumberFormatException{
        return Double.parseDouble(textField2.getText());
    }    


    public void quitte(){
        Platform.exit();
    }

    private void ajouteChamp(Pane root){
        HBox hbChamp1 = new HBox(20);
        Label label1 = new Label();
        this.textField1 = new TextField();
        hbChamp1.getChildren().addAll(label1, this.textField1);

        HBox hbChamp2 = new HBox(20);
        Label label2 = new Label();
        this.textField2 = new TextField();
        hbChamp2.getChildren().addAll(label2, this.textField2);

        
        // On connecte un controleur       
        HBox hbChamps = new HBox(3);
        hbChamps.setPadding(new Insets(10, 10, 10, 10));

        hbChamps.getChildren().addAll(hbChamp1, hbChamp2);
        hbChamps.setAlignment(Pos.BASELINE_CENTER);
        root.getChildren().add(hbChamps);
    }

    private void ajouteBoutons(Pane root){
        HBox hbButtons = new HBox(3);
        hbButtons.setPadding(new Insets(10, 10, 10, 10));

        // On connecte des controleurs        
        this.addButton.setOnAction(new ControleurBoutonAdd(this, this.resultat));
        this.subButton.setOnAction(new ControleurBoutonSub(this, this.resultat));
        
        hbButtons.getChildren().addAll(this.addButton, this.subButton);
        hbButtons.setAlignment(Pos.BASELINE_CENTER);
        root.getChildren().add(hbButtons);
    }

    public static void main(String[] args) {
        launch(args);
    }
}
