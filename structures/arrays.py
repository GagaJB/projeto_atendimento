class VetorNaoOrdenado:
    def __init__(self):
        self.elementos = []

    def inserir(self, elemento):
        self.elementos.append(elemento)

    def buscar(self, id_cliente):
        for el in self.elementos:
            if el.id_cliente == id_cliente:
                return el
        return None

    def get_todos(self):
        return self.elementos

class VetorOrdenado:
    def __init__(self):
        self.elementos = []

    def inserir(self, elemento):
        self.elementos.append(elemento)
        self._ordenar()

    def _ordenar(self):
        n = len(self.elementos)
        for i in range(1, n):
            chave = self.elementos[i]
            j = i - 1
            while j >= 0 and self.elementos[j].id_cliente > chave.id_cliente:
                self.elementos[j + 1] = self.elementos[j]
                j -= 1
            self.elementos[j + 1] = chave

    def busca_binaria(self, id_cliente):
        esq = 0
        dir = len(self.elementos) - 1

        while esq <= dir:
            meio = (esq + dir) // 2
            if self.elementos[meio].id_cliente == id_cliente:
                return self.elementos[meio]
            elif self.elementos[meio].id_cliente < id_cliente:
                esq = meio + 1
            else:
                dir = meio - 1
        return None