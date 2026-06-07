# Sistema Completo de Atendimento e Análise

## Objetivo
Este projeto consiste em um software de gerenciamento de atendimentos para clínicas ou centrais de atendimento. Ele foi desenvolvido com foco na aplicação prática de Estruturas de Dados e Algoritmos, incluindo vetores, listas encadeadas, pilhas, filas, recursão e ordenação.

## Funcionalidades e Requisitos Atendidos
- **Cadastros:** Clientes (com ou sem prioridade) e Atendentes.
- **Filas de Atendimento:** Fila comum e fila de prioridade, respeitando a ordem de chegada e a regra de um cliente por atendente.
- **Histórico e Reversão:** Registro completo de atendimentos finalizados e possibilidade de desfazer a última finalização utilizando uma Pilha.
- **Relatórios (Incluindo Extras):**
  - Tempo médio de atendimento.
  - Exportação de histórico para formato CSV.
  - Top 5 clientes mais atendidos (utilizando algoritmo Quick Sort).
  - Filtro de histórico por data (utilizando Busca Recursiva).
  - Alerta de tempo de espera alto com base no tamanho atual da fila.

## Arquitetura e Estruturas de Dados
O código foi modularizado nas seguintes camadas:
- `models/`: Entidades base (Cliente, Atendente).
- `structures/`: Estruturas criadas do zero (Fila de Prioridade, Pilha, Lista Encadeada, Vetor Ordenado para Busca Binária e Vetor Não Ordenado).
- `services/`: Regras de negócio e controle de estado.
- `utils/`: Algoritmos de ordenação/recursão e gerenciamento de arquivos.

## Como Executar o Sistema

1. Certifique-se de ter o Python instalado na sua máquina (versão 3.6 ou superior).
2. Clone o repositório para a sua máquina executando o comando abaixo:
   ```bash
   git clone [https://github.com/GagaJB/projeto_atendimento.git](https://github.com/GagaJB/projeto_atendimento.git)
   ```
3. Acesse a pasta raiz do projeto:
   ```bash
   cd projeto_atendimento
   ```
4. Execute o arquivo principal pelo terminal:
   ```bash
   python main.py
   ```
5. Navegue pelo menu numérico no terminal. Os dados são salvos automaticamente ao escolher a opção "Salvar e Sair".

## Como Executar os Testes Unitários

Para validar o funcionamento isolado das estruturas de dados (Fila, Pilha e Vetor Ordenado), execute o comando abaixo na raiz do projeto:
```bash
python -m unittest tests/test_structures.py
```

---
**Autores:** Gabriel de Jesus, Arthur Augusto, Isaque Rocha, Kaio Vinicyus, Nicolas Pereira