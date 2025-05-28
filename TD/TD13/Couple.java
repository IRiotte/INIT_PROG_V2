public class Couple<T extends Comparable<T>> implements Comparable<Couple<T>>{
    private T premier, second;

    public Couple(T premier, T second){
        this.premier = premier;
        this.second = second;
    }

    @Override
    public int compareTo(Couple<T> couple){
        return this.premier.compareTo(couple.premier);
    }
}
