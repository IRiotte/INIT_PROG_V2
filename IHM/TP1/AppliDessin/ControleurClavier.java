import javafx.scene.input.KeyEvent;
import javafx.scene.input.KeyCode;
import javafx.event.EventHandler;

public class ControleurClavier implements EventHandler<KeyEvent>{
    private AppliDessin appli;
    
    public ControleurClavier(AppliDessin appli){
        this.appli = appli;
    }
    
    public void handle(KeyEvent e){       
        if (e.getCode().equals(KeyCode.ADD) || e.getCode().equals(KeyCode.EQUALS)){
            System.out.println("+");
            appli.augmenteSlider();;
        }

        if (e.getCode().equals(KeyCode.SUBTRACT) || e.getCode().equals(KeyCode.MINUS)){
            System.out.println("-");
            appli.diminueSlider();
        }

        if (e.getCode().equals(KeyCode.MULTIPLY)){
            System.out.println("*");
            appli.chanegCouleurCercle();
        }
    }
}
