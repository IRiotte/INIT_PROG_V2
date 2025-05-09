import java.util.List;
import java.util.ArrayList;

public class Siege {
    private int numero;
    private List<Reservation> reservations;


    public Siege(int numero){
        this.numero = numero;
        this.reservations = new ArrayList<>();
    }

    public boolean estLibre(String date){
        for (Reservation res : this.reservations){
            if (res.getDate().equals(date)){
                return false;
            }
        }
        return true;
    }

    public void addReservation(Reservation reserv){
        this.reservations.add(reserv);
    }

    public List<Reservation> getReservations(){
        return this.reservations;
    }

    public int getNumero(){
        return this.numero;
    }
}
