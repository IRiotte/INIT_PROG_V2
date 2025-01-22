public class ExecutablePokemon {
    public static void main(String [] args) {
        Pokemon poke; /*Définition du type de la variable*/
        poke = new Pokemon("Bulbizarre", 30); /*Affectation d'une nouvelle instance de Pokemon à poke*/
        poke.evoluer("Herbizarre", 37); /*appel de la methode evoluer n°1 (2 args)*/
        poke.evoluer("Florizarre"); /*appel de la methode evoluer n°2 (1 arg)*/
        System.out.println(poke.toString()); // (1)

        Pokemon poke_nouv;
        poke_nouv = new Pokemon("Abo", 10);
        poke_nouv.evoluer("Arbok", 24);
        System.out.println(poke_nouv.toString());
    }
}