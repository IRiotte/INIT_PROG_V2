import javafx.event.EventHandler;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;

public class ControleurAdd implements EventHandler<KeyEvent>{ 

    private Resultat resultat;
    private AppliConverter appli;
    
    public ControleurAdd(Resultat res, AppliConverter appli){
        this.resultat = res;
        this.appli = appli;
    }

    @Override
    public void handle(KeyEvent e) {
        /*if (e.getCode().equals(KeyCode.ENTER)){
            double value;
            double value2;
            try{
                value = this.appli.getValueCelcius();
                value2 = this.appli.getValueKelvin();
                this.temperature.setvaleurCelcius(value);
                this.temperature.setvaleurKelvin(value2);
                this.appli.majTF();                
            }
            catch (NumberFormatException exp) {
                this.appli.effaceTF();
            }
          } else{
              //nothing
          }*/
    }
          
}
