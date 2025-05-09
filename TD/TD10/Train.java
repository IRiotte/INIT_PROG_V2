import java.util.List;
import java.util.ArrayList;

public class Train {
    private List<Wagon> wagons;

    public Train(){
        this.wagons = new ArrayList<>();
    }

    public List<Siege> getListeSiegesLibre(int classe, String date){
        List<Siege> siegesLibres = new ArrayList<>();
        for (Wagon wagon : this.wagons){
            if (wagon.getClasse() == classe){
                for (Siege siege : wagon.getSiegesLibres(date)){
                    siegesLibres.add(siege);
                }
            }
        }
        return siegesLibres;
    }

    public List<Wagon> getWagons(){
        
        return this.wagons;
    }

    public void reserver(int classe, String date, Client client) throws PlusDePlaceException {
        List<Siege> siegesLibres = this.getListeSiegesLibre(classe, date);
        if (siegesLibres.size() > 0){
            siegesLibres.get(0).addReservation(new Reservation(date, client));
        }
        else{
            throw new PlusDePlaceException();
        }
    }

    public void ajouterWagon(Wagon wagon){
        this.wagons.add(wagon);
    }
    
}