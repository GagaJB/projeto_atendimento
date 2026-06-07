class Cliente:
    def __init__(self, id_cliente, nome, telefone, prioridade):
        self.id_cliente = id_cliente
        self.nome = nome
        self.telefone = telefone
        self.prioridade = prioridade

    def __str__(self):
        return f"[{self.id_cliente}] {self.nome} - Tel: {self.telefone} | Prioridade: {self.prioridade}"