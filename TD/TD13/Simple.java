public class Simple<T> {
    private T contenu;

    public Simple(){
        this.contenu = null;
    }

    public Simple(T contenu){
        this.contenu = contenu;
    }

    public T getContenu(){
        return this.contenu;
    }

    public void setContenu(T contenu){
        this.contenu = contenu;
    }
}
