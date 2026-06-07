import csv
import pickle
import os

def exportar_csv(nome_arquivo, dados, cabecalhos):
    try:
        with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(cabecalhos)
            for linha in dados:
                writer.writerow(linha)
        return True
    except Exception:
        return False

def salvar_estado(dados, nome_arquivo="dados_sistema.pkl"):
    with open(nome_arquivo, 'wb') as file:
        pickle.dump(dados, file)

def carregar_estado(nome_arquivo="dados_sistema.pkl"):
    if not os.path.exists(nome_arquivo):
        return None
    with open(nome_arquivo, 'rb') as file:
        return pickle.load(file)