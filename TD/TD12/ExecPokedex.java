public class ExecPokedex {
    public static void main(String[] args){

        Pokedex pokedex = new Pokedex();
        
        pokedex.ajouter(Attaque.Feu, "Dracofeu");
        pokedex.ajouter(Attaque.Feu, "Salameche");
        pokedex.ajouter(Attaque.Eau, "Palkia");

        System.out.println(pokedex.appartient("Palkia"));
        System.out.println(pokedex.appartient("rien"));


        
    }
}
