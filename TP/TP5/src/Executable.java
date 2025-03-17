public class Executable {
    public static void main(String[] args) {
        WeekEnd weekEndMai = new WeekEnd("Mai");
        weekEndMai.ajouteParticipant("Davy", 37);
        weekEndMai.ajouteParticipant("Elie", 27);
        weekEndMai.ajouteParticipant("Gaby", 24);
        weekEndMai.ajouteParticipant("Anna", 31);

        weekEndMai.ajouteDepense(12, "pain", "Davy", 37);
        weekEndMai.ajouteDepense(100, "pizzas", "Elie", 27);
        weekEndMai.ajouteDepense(70, "essence", "Davy", 37);
        weekEndMai.ajouteDepense(15, "vin", "Gaby", 24);
        weekEndMai.ajouteDepense(10, "vin", "Elie", 27);

        Personne davy = new Personne("Davy", 37);
        Personne elie = new Personne("Elie", 27);
        Personne gaby = new Personne("Gaby", 24);
        Personne anna = new Personne("Anna", 31);

        assert weekEndMai.totalDepense(davy) == 82;
        assert weekEndMai.totalDepense(elie) == 110;
        assert weekEndMai.totalDepense(gaby) == 15;
        assert weekEndMai.totalDepense(anna) == 0;

        assert weekEndMai.avoirPersonne(davy) == 82 - (207 / 4);
        assert weekEndMai.avoirPersonne(elie) == 110 - (207 / 4);
        assert weekEndMai.avoirPersonne(gaby) == 15 - (207 / 4);
        assert weekEndMai.avoirPersonne(anna) == 0 - (207 / 4);

        WeekEnd weekEndJuin = new WeekEnd("Juin");
        weekEndJuin.ajouteParticipant("Davy", 37);
        weekEndJuin.ajouteParticipant("Gaby", 24);
        weekEndJuin.ajouteParticipant("Anna", 31);
        weekEndJuin.ajouteParticipant("Billy", 16);
        weekEndJuin.ajouteParticipant("Sasha", 21);

        weekEndJuin.ajouteDepense(15, "fromage", "Davy", 37);
        weekEndJuin.ajouteDepense(12, "pain", "Davy", 37);
        weekEndJuin.ajouteDepense(20, "vin", "Gaby", 24);
        weekEndJuin.ajouteDepense(34, "glaces", "Gaby", 24);
        weekEndJuin.ajouteDepense(52, "pizzas", "Anna", 31);
        weekEndJuin.ajouteDepense(8, "pistaches", "Anna", 31);
        weekEndJuin.ajouteDepense(8, "film", "Davy", 37);
        weekEndJuin.ajouteDepense(3, , null, 0);
}
