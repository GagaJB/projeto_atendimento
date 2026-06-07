import csv

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