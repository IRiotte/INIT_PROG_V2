import javafx.event.EventHandler;
import javafx.event.ActionEvent;


public class ControleurBoutonConvertF implements EventHandler<ActionEvent>{ 

    private Temperature temperature;
    private AppliConverter appli;
    
    public ControleurBoutonConvertF(AppliConverter appli, Temperature temperature){
        this.appli = appli;
        this.temperature = temperature;
    }

    @Override
    public void handle(ActionEvent event) {
        double value;
        try{
            value = this.appli.getValueFahrenheit();
            this.temperature.setvaleurFahrenheit(value);
            this.appli.majTF();                
        }
        catch (NumberFormatException exp) {
            this.appli.effaceTF();
        }
    }
}