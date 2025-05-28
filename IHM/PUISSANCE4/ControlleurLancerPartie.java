import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.scene.control.Button;
import javafx.scene.control.ButtonType;
import javafx.scene.layout.BorderPane;

import java.util.Optional;


public class ControlleurLancerPartie implements EventHandler<ActionEvent> {
    
    private BorderPane root;

    public ControlleurLancerPartie() {
        this.root = FXMLLoader.load(getClass().getResource("SayHello.fxml"));;
    }


    /**
     * L'action consiste à retourner sur la page d'accueil. Il faut vérifier qu'il n'y avait pas une partie en cours
     * @param actionEvent l'événement action
     */
    @Override
    public void handle(ActionEvent actionEvent) {
        
        vuePendu.modeAccueil();  
        System.out.println("retour accueil");
        
        
    }
}
