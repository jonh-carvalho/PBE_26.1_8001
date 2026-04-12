class Aluno:
    def __init__(self, nome, matricula, notas=None):
        self.nome = nome
        self.matricula = matricula
        self.notas = notas if notas is not None else []
    
    def __str__(self):
        return f"Aluno: {self.nome}, Matrícula: {self.matricula}, Média: {self.calcular_media():.2f}"