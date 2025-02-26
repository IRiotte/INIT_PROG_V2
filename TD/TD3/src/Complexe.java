public class Complexe {
    private int premier;
    private int second;

    public Complexe(int val1, int val2) {
        this.premier = val1;
        this.second = val2;
    }

    public int getPartieReelle(){
        return this.premier;
    }

    public int getPartieImaginaire(){
        return this.second;
    }

    public Complexe plus(Complexe complexe){
        int premier = this.premier + complexe.premier;
        int second = this.second + complexe.second;
        return  new Complexe(premier, second);
    }

    public Complexe produit(Complexe complexe){
        int premier = (this.premier * complexe.premier) - (this.second * complexe.second);
        int second = (this.premier * complexe.second) + (this.second * complexe.premier);
        return new Complexe(premier, second);
    }


    @Override
    public boolean equals(Object objet){
        if (objet == null) {return false;}
        if (objet == this) {return true;}
        if (! (objet instanceof Complexe)) {return false;}

        Complexe tmp = (Complexe) objet;
        return this.premier == tmp.premier && this.second == tmp.second;
    }

    @Override
    public String toString() {
        return this.premier + " + " + this.second + "i";
    }
}
