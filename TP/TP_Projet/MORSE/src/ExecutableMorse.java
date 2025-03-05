public class ExecutableMorse {
    public static void main(String[] args) {
        Lettre n = new Lettre('N');
        assert n.toChar() == 'N';
        assert n.toMorse().equals("===_=");
        System.out.println(n.toMorse());
        Lettre a = new Lettre('A');
        assert a.toMorse().equals("=_===");
        System.out.println(a.toMorse());
        assert a.toChar() == 'A';

        Texte texte = new Texte("TO TO");
        System.out.println(texte.toMorse());
        System.out.println(texte.decode(texte.toMorse()));
        Texte texte1 = new Texte("GA BU");
        System.out.println(texte1.toMorse());
        System.out.println(texte1.decode(texte1.toMorse()));
        
    }
    
}
