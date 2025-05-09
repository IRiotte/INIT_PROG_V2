import javafx.event.EventHandler;
import javafx.event.ActionEvent;


public class ControleurBoutonAdd implements EventHandler<ActionEvent>{ 

    private AppliConverter appli;
    
    public ControleurBoutonAdd(AppliConverter appli, Resultat res){
        this.appli = appli;
    }

    @Override
    public void handle(ActionEvent event) {
        /*
        double value;
        try{
            value = this.appli.getValueFahrenheit();
            this.temperature.setvaleurFahrenheit(value);
            this.appli.majTF();                
        }
        catch (NumberFormatException exp) {
            this.appli.effaceTF();
        }*/
    }
}