public class CoupleDouble implements Comparable<CoupleDouble> {
    private double premier, second; 

    public CoupleDouble(double premier, double second){
        this.premier = premier;
        this.second = second;
    }

    @Override
    public int compareTo(CoupleDouble cplEnt) {
        if (this.premier < cplEnt.premier) {return -1;} 
        if (this.premier > cplEnt.premier) {return 1;} 
        return 0;
    }
}
