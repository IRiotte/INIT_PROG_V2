public class ExecCouple {
    public static void main(String[] args){

        Couple<Integer> coupleEntier1 = new Couple<>(1,2);
        Couple<Integer> coupleEntier2 = new Couple<>(1,2);

        System.out.println(coupleEntier1.equals(coupleEntier2));

        Couple<Double> coupleDouble1 = new Couple<>(1.2,2.8);
        Couple<Double> coupleDouble2 = new Couple<>(0.4,7.7);Override

        System.out.println(coupleDouble1.equals(coupleDouble2));

    }
}
