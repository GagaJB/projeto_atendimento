import datetime
from models.cliente import Cliente
from models.atendente import Atendente
from structures.queues import FilaAtendimento
from structures.stack import Pilha
from structures.linked_list import LinkedList
from structures.arrays import VetorOrdenado, VetorNaoOrdenado

class AtendimentoService:
    def __init__(self):
        self.clientes_cadastrados = VetorOrdenado()
        self.atendentes_cadastrados = VetorNaoOrdenado()
        self.clientes_ativos = LinkedList()
        self.fila = FilaAtendimento()
        self.historico_desfazer = Pilha()
        self.historico_geral = []
        self.atendimentos_em_andamento = {}

    def cadastrar_cliente(self, id_cliente, nome, telefone, prioridade):
        if self.clientes_cadastrados.busca_binaria(id_cliente):
            return False
        novo_cliente = Cliente(id_cliente, nome, telefone, prioridade)
        self.clientes_cadastrados.inserir(novo_cliente)
        return True

    def cadastrar_atendente(self, id_atendente, nome):
        if self.atendentes_cadastrados.buscar(id_atendente):
            return False
        novo_atendente = Atendente(id_atendente, nome)
        self.atendentes_cadastrados.inserir(novo_atendente)
        return True

    def abrir_atendimento(self, id_cliente):
        cliente = self.clientes_cadastrados.busca_binaria(id_cliente)
        if not cliente:
            return False
        self.clientes_ativos.append(cliente)
        self.fila.enqueue(cliente)
        return True

    def chamar_proximo(self, id_atendente):
        atendente = self.atendentes_cadastrados.buscar(id_atendente)
        if not atendente or self.fila.is_empty():
            return None
        if id_atendente in self.atendimentos_em_andamento:
            return False 
        
        cliente = self.fila.dequeue()
        self.atendimentos_em_andamento[id_atendente] = {
            "cliente": cliente,
            "inicio": datetime.datetime.now()
        }
        return cliente

    def finalizar_atendimento(self, id_atendente):
        if id_atendente not in self.atendimentos_em_andamento:
            return None
        
        dados = self.atendimentos_em_andamento.pop(id_atendente)
        cliente = dados["cliente"]
        fim = datetime.datetime.now()
        duracao = (fim - dados["inicio"]).total_seconds() / 60.0 
        
        registro = {
            "id_cliente": cliente.id_cliente,
            "nome_cliente": cliente.nome,
            "id_atendente": id_atendente,
            "data": fim.strftime("%Y-%m-%d"),
            "hora": fim.strftime("%H:%M:%S"),
            "duracao_minutos": round(duracao, 2)
        }
        self.historico_geral.append(registro)
        self.historico_desfazer.push(registro)
        self.clientes_ativos.remove(cliente.id_cliente)
        return registro

    def desfazer_ultima_finalizacao(self):
        if self.historico_desfazer.is_empty():
            return None
        ultimo_registro = self.historico_desfazer.pop()
        self.historico_geral.remove(ultimo_registro)
        
        cliente = self.clientes_cadastrados.busca_binaria(ultimo_registro["id_cliente"])
        if cliente:
            self.clientes_ativos.append(cliente)
            self.fila.enqueue(cliente) 
        return ultimo_registro

    def remover_cliente_inativo(self, id_cliente):
        cliente = self.clientes_cadastrados.busca_binaria(id_cliente)
        if not cliente:
            return False
        em_espera = any(c.id_cliente == id_cliente for c in self.fila.fila_comum + self.fila.fila_prioridade)
        em_atendimento = any(d["cliente"].id_cliente == id_cliente for d in self.atendimentos_em_andamento.values())
        
        if em_espera or em_atendimento:
            return False
            
        return self.clientes_ativos.remove(id_cliente)