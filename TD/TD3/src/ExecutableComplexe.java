public class ExecutableComplexe {
    public static void main(String[] args) {
        Complexe z1 = new Complexe(4, 3);

        assert z1.getPartieReelle() == 4;
        assert z1.getPartieImaginaire() == 3;

        Complexe z2 = new Complexe(1, 2);

        assert z2.getPartieReelle() == 1;
        assert z2.getPartieImaginaire() == 2;

        Complexe z3 = new Complexe(5, 5);
        assert z1.plus(z2).equals(z3);

        Complexe z4 = new Complexe(-2, 11);
        assert z1.produit(z2).equals(z4);

    }
    

}
