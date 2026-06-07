from utils.algorithms import quick_sort, filtrar_por_data_recursivo
from utils.file_manager import exportar_csv

class ReportService:
    def __init__(self, historico_geral):
        self.historico_geral = historico_geral

    def tempo_medio_atendimento(self):
        if not self.historico_geral:
            return 0.0
        total_minutos = sum(registro["duracao_minutos"] for registro in self.historico_geral)
        return round(total_minutos / len(self.historico_geral), 2)

    def top_5_clientes(self):
        contagem = {}
        for reg in self.historico_geral:
            id_c = reg["id_cliente"]
            if id_c not in contagem:
                contagem[id_c] = {"id_cliente": id_c, "nome": reg["nome_cliente"], "qtd": 0}
            contagem[id_c]["qtd"] += 1
        
        lista_contagem = list(contagem.values())
        ordenados = quick_sort(lista_contagem, lambda x: x["qtd"], reverse=True)
        return ordenados[:5]

    def filtrar_por_data(self, data_alvo):
        return filtrar_por_data_recursivo(self.historico_geral, data_alvo)

    def alerta_tempo_espera(self, tamanho_fila, limite_minutos=30):
        tempo_medio = self.tempo_medio_atendimento()
        tempo_estimado = tamanho_fila * tempo_medio
        
        if tempo_estimado > limite_minutos:
            return True, tempo_estimado
        return False, tempo_estimado

    def exportar_historico(self, nome_arquivo="historico.csv"):
        if not self.historico_geral:
            return False
        
        cabecalhos = ["ID Cliente", "Nome", "ID Atendente", "Data", "Hora", "Duracao (min)"]
        dados_formatados = [
            [r["id_cliente"], r["nome_cliente"], r["id_atendente"], r["data"], r["hora"], r["duracao_minutos"]]
            for r in self.historico_geral
        ]
        
        return exportar_csv(nome_arquivo, dados_formatados, cabecalhos)