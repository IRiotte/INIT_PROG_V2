import javafx.event.EventHandler;
import javafx.event.ActionEvent;


public class ControleurBoutonConvertC implements EventHandler<ActionEvent>{ 

    private Temperature temperature;
    private AppliConverter appli;
    
    public ControleurBoutonConvertC(AppliConverter appli, Temperature temperature){
        this.temperature = temperature;
        this.appli = appli;
    }

    @Override
    public void handle(ActionEvent event) {
        double value;
        try{
            value = this.appli.getValueCelcius();
            this.temperature.setvaleurCelcius(value);
            this.appli.majTF();                
        }
        catch (NumberFormatException exp) {
            this.appli.effaceTF();
        }
    }
}
