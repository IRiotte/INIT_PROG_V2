public class Reservation {
    private String date;
    private Client client;

    public Reservation(String date, Client client){
        this.date = date;
        this.client = client;
    }

    public String getDate(){
        return this.date;
    }
}
