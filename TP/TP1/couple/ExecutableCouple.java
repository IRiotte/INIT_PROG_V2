public class ExecutableCouple {
    public static void main(String [] args) {
        Couple unCouple = new Couple(5, -4);
        System.out.println(unCouple.toString()); // (1)
        System.out.println(unCouple.somme()); // (2)

        System.out.println(unCouple.produit());

        Couple unAutreCouple = new Couple();
        unAutreCouple.setPremier(7);
        unAutreCouple.permuter();
        System.out.println(unAutreCouple.toString()); // (3)

        Couple autreCouple = new Couple(6);
        System.out.println(autreCouple.toString());


        Couple exemple;
        exemple = new Couple(3, -8);
        assert exemple.somme() == -5;     // FAUX !!!
        assert exemple.produit() == -24;
        exemple = new Couple();
        assert exemple.somme() == 0;
        assert exemple.produit() == 0;
        exemple = new Couple(7);
        assert exemple.somme() == 14;
        assert exemple.produit() == 49;
    }
}

/*
1) Seule la classe ExecutableCouplle est exécutable car elle possède une méthode main()

2) Attributs: premier (int), second (int)
    Constructeur: Couple() et Couple(int x, int y)
    Methodes: setPremier(int premier), permuter(), somme(), toString()

3)  1)- (5,-4)
    2) - 1
    3) - (0,7)

4) javac ExecutableCouple.java
5) java ExecutableCouple
*/