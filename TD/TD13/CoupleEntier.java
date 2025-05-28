public class CoupleEntier implements Comparable<CoupleEntier> {
    private int premier, second; 

    public CoupleEntier(int premier, int second){
        this.premier = premier;
        this.second = second;
    }

    @Override
    public int compareTo(CoupleEntier cplEnt){
        if (this.premier < cplEnt.premier) {return -1;}
        if (this.premier > cplEnt.premier) {return 1;}
        if (this.second < cplEnt.second) {return -1;}
        if (this.second > cplEnt.second) {return 1;}
        return 0;
    }
}
