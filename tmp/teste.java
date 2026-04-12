public class Aluno {
    private int id;
    private String nome;
    private String email;
    private double nota;

    public Aluno(int id, String nome, String email, double nota) {
        this.id = id;
        this.nome = nome;
        this.email = email;
        this.nota = nota;
    }
    

    @Override
    public String toString() {
        return "Aluno{" +
                "id=" + id +
                ", nome='" + nome + '\'' +
                ", email='" + email + '\'' +
                ", nota=" + nota +
                '}';
    }
}