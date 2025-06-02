import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.scene.control.RadioButton;

/**
 * Controleur des radio boutons gérant le niveau
 */
public class ControleurNiveau implements EventHandler<ActionEvent> {

    /**
     * modèle du jeu
     */
    private MotMystere modelePendu;


    /**
     * @param modelePendu modèle du jeu
     */
    public ControleurNiveau(MotMystere modelePendu) {
        this.modelePendu = modelePendu;
    }

    /**
     * gère le changement de niveau
     * @param actionEvent
     */
    @Override
    public void handle(ActionEvent actionEvent) {
        RadioButton radiobouton = (RadioButton) actionEvent.getTarget();
        switch (radiobouton.getText()) {
            case "Facile":
                modelePendu.setNiveau(MotMystere.FACILE);
                break;
            case "Moyen":
                modelePendu.setNiveau(MotMystere.MOYEN);
                break;
            case "Difficile":
                modelePendu.setNiveau(MotMystere.DIFFICILE);
                break;
            case "Hardcore":
                modelePendu.setNiveau(MotMystere.EXPERT);
                break;

        }
        
        String nomDuRadiobouton = radiobouton.getText();
        System.out.println(nomDuRadiobouton);
    }
}
