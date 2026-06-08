import unittest
from models.cliente import Cliente
from structures.queues import FilaAtendimento
from structures.stack import Pilha
from structures.arrays import VetorOrdenado

class TestStructures(unittest.TestCase):
    def test_fila_prioridade(self):
        fila = FilaAtendimento()
        c1 = Cliente(1, "Ana", "111", False)
        c2 = Cliente(2, "Beto", "222", True)
        fila.enqueue(c1)
        fila.enqueue(c2)
        self.assertEqual(fila.dequeue().id_cliente, 2)

    def test_pilha(self):
        pilha = Pilha()
        pilha.push("A")
        pilha.push("B")
        self.assertEqual(pilha.pop(), "B")

    def test_busca_binaria(self):
        vetor = VetorOrdenado()
        c1 = Cliente(10, "Carlos", "333", False)
        c2 = Cliente(5, "Diana", "444", False)
        vetor.inserir(c1)
        vetor.inserir(c2)
        encontrado = vetor.busca_binaria(5)
        self.assertIsNotNone(encontrado)
        self.assertEqual(encontrado.nome, "Diana")

if __name__ == '__main__':
    unittest.main()