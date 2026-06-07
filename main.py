from services.attendance_service import AtendimentoService
from services.report_service import ReportService
from utils.file_manager import salvar_estado, carregar_estado

def exibir_menu():
    print("\n--- SISTEMA DE ATENDIMENTO ---")
    print("1. Cadastrar Cliente")
    print("2. Cadastrar Atendente")
    print("3. Abrir Atendimento (Entrar na Fila)")
    print("4. Chamar Proximo da Fila")
    print("5. Finalizar Atendimento")
    print("6. Desfazer Ultima Finalizacao")
    print("7. Relatorios e Extras")
    print("8. Salvar e Sair")
    return input("Escolha uma opcao: ")

def menu_relatorios(report_service, attendance_service):
    print("\n--- RELATORIOS ---")
    print("1. Tempo Medio de Atendimento")
    print("2. Top 5 Clientes")
    print("3. Filtrar Historico por Data")
    print("4. Status da Fila (Alertas)")
    print("5. Exportar Historico CSV")
    
    op = input("Opcao: ")
    if op == "1":
        print(f"Tempo Medio: {report_service.tempo_medio_atendimento()} minutos")
    elif op == "2":
        top5 = report_service.top_5_clientes()
        for i, c in enumerate(top5):
            print(f"{i+1}. [{c['id_cliente']}] {c['nome']} - {c['qtd']} atendimentos")
    elif op == "3":
        data = input("Digite a data (YYYY-MM-DD): ")
        resultados = report_service.filtrar_por_data(data)
        for r in resultados:
            print(r)
    elif op == "4":
        tamanho = len(attendance_service.fila.fila_comum) + len(attendance_service.fila.fila_prioridade)
        alerta, tempo = report_service.alerta_tempo_espera(tamanho)
        print(f"Fila atual: {tamanho} pessoas. Tempo estimado: {tempo} minutos.")
        if alerta:
            print("ALERTA: TEMPO DE ESPERA ALTO!")
    elif op == "5":
        if report_service.exportar_historico():
            print("Historico exportado para historico.csv")
        else:
            print("Erro ao exportar.")

def main():
    estado_salvo = carregar_estado()
    if estado_salvo:
        service = estado_salvo
        print("Dados carregados com sucesso!")
    else:
        service = AtendimentoService()

    while True:
        opcao = exibir_menu()

        try:
            if opcao == "1":
                id_c = int(input("ID do Cliente (numero): "))
                nome = input("Nome: ")
                telefone = input("Telefone: ")
                prio = input("Prioridade (S/N): ").strip().upper() == "S"
                if service.cadastrar_cliente(id_c, nome, telefone, prio):
                    print("Cliente cadastrado.")
                else:
                    print("ID ja existe.")
            
            elif opcao == "2":
                id_a = int(input("ID do Atendente (numero): "))
                nome = input("Nome: ")
                if service.cadastrar_atendente(id_a, nome):
                    print("Atendente cadastrado.")
                else:
                    print("ID ja existe.")

            elif opcao == "3":
                id_c = int(input("ID do Cliente: "))
                if service.abrir_atendimento(id_c):
                    print("Cliente adicionado a fila.")
                else:
                    print("Cliente nao encontrado.")

            elif opcao == "4":
                id_a = int(input("ID do Atendente: "))
                cliente = service.chamar_proximo(id_a)
                if cliente is False:
                    print("Atendente ja esta em um atendimento.")
                elif cliente:
                    print(f"Atendendo: {cliente.nome}")
                else:
                    print("Fila vazia ou atendente nao encontrado.")

            elif opcao == "5":
                id_a = int(input("ID do Atendente: "))
                reg = service.finalizar_atendimento(id_a)
                if reg:
                    print(f"Atendimento finalizado. Duracao: {reg['duracao_minutos']} min")
                else:
                    print("Nenhum atendimento em andamento para este atendente.")

            elif opcao == "6":
                reg = service.desfazer_ultima_finalizacao()
                if reg:
                    print(f"Finalizacao do cliente {reg['nome_cliente']} desfeita.")
                else:
                    print("Historico vazio.")

            elif opcao == "7":
                report_service = ReportService(service.historico_geral)
                menu_relatorios(report_service, service)

            elif opcao == "8":
                salvar_estado(service)
                print("Dados salvos. Saindo...")
                break
            else:
                print("Opcao invalida.")
        except ValueError:
            print("Erro de entrada. Digite valores numericos quando solicitado.")

if __name__ == "__main__":
    main()