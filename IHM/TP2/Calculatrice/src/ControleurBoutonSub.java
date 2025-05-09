import javafx.event.EventHandler;
import javafx.event.ActionEvent;


public class ControleurBoutonSub implements EventHandler<ActionEvent>{ 

    private AppliConverter appli;

    public ControleurBoutonSub(AppliConverter appli, Resultat res){
        this.appli = appli;
    }

    @Override
    public void handle(ActionEvent event) {
        /* double value;
        try{
            value = this.appli.getValueKelvin();
            this.temperature.setvaleurKelvin(value);
            this.appli.majTF();                
        }
        catch (NumberFormatException exp) {
            this.appli.effaceTF();
        }*/
    }
}