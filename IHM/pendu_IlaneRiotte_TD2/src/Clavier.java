import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.control.Button;
import javafx.scene.layout.TilePane;
import javafx.scene.shape.Circle ;
import java.util.ArrayList;
import java.util.List;
import java.util.Set;
import javax.swing.border.Border;

/**
 * Génère la vue d'un clavier et associe le contrôleur aux touches
 * le choix ici est d'un faire un héritié d'un TilePane
 */
public class Clavier extends TilePane{

    private List<Button> clavier;

    /**
     * constructeur du clavier
     * @param touches une chaine de caractères qui contient les lettres à mettre sur les touches
     * @param actionTouches le contrôleur des touches
     * @param tailleLigne nombre de touches par ligne
     */
    public Clavier(String touches, EventHandler<ActionEvent> actionTouches) {
        this.clavier = new ArrayList<>();
        for (char carac : touches.toCharArray()){
            Button touche = new Button("" + carac);
            touche.setMinSize(55, 50);
            touche.setMaxSize(55, 50);
            touche.setStyle("-fx-background-radius: 10000;");
            touche.setOnAction(actionTouches);
            clavier.add(touche);
            this.getChildren().add(touche);
        }
    }

    /**
     * permet de désactiver certaines touches du clavier (et active les autres)
     * @param touchesDesactivees une chaine de caractères contenant la liste des touches désactivées
     */
    public void desactiveTouches(Set<String> touchesDesactivees){
        for (Button touche : clavier) {
            if (touchesDesactivees.contains(touche.getText())) {
                touche.setDisable(true);
            } else {
                touche.setDisable(false);
            }
        }
    }

    public void desactiveToutesLesTouches(){
        for (Button touche : clavier) {
            touche.setDisable(true);
        }
    }
}
