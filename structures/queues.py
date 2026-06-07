class FilaAtendimento:
    def __init__(self):
        self.fila_comum = []
        self.fila_prioridade = []

    def enqueue(self, cliente):
        if cliente.prioridade:
            self.fila_prioridade.append(cliente)
        else:
            self.fila_comum.append(cliente)

    def dequeue(self):
        if self.fila_prioridade:
            return self.fila_prioridade.pop(0)
        if self.fila_comum:
            return self.fila_comum.pop(0)
        return None

    def is_empty(self):
        return len(self.fila_prioridade) == 0 and len(self.fila_comum) == 0