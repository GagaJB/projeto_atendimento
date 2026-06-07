class Atendente:
    def __init__(self, id_atendente, nome):
        self.id_atendente = id_atendente
        self.nome = nome

    def __str__(self):
        return f"[{self.id_atendente}] {self.nome}"