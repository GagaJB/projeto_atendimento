# Relatório Técnico - Sistema Completo de Atendimento

## Estrutura e Decisões Técnicas
O projeto adotou uma arquitetura modularizada, separando rigorosamente as camadas de dados (Models), estruturas de dados (Structures), regras e lógicas de negócio (Services) e utilitários/interface (Utils e Main).

## Estruturas de Dados e Análise Big-O

1. **Vetor Ordenado (com Busca Binária)**
   - **Utilização:** Cadastro de clientes para rápida localização por ID.
   - **Complexidade:** Busca binária executada em $O(\log n)$. A inserção adaptada realiza a ordenação com complexidade de $O(n)$ no deslocamento interno.

2. **Vetor Não Ordenado**
   - **Utilização:** Cadastro de atendentes e buscas lineares simples.
   - **Complexidade:** Inserção em tempo constante $O(1)$. Busca linear com complexidade $O(n)$.

3. **Fila Comum e Fila de Prioridade**
   - **Utilização:** Controle do fluxo para a chamada e gerenciamento do sistema de senhas.
   - **Complexidade:** Inserção em $O(1)$ amortizado. Remoção em $O(n)$ devido ao recálculo dos índices das listas subjacentes.

4. **Pilha**
   - **Utilização:** Gerenciamento do histórico para a funcionalidade "Desfazer Última Finalização".
   - **Complexidade:** Operações de empilhar e desempilhar ocorrem estritamente em $O(1)$.

5. **Lista Encadeada**
   - **Utilização:** Gerenciamento e persistência temporária dos clientes ativos do dia.
   - **Complexidade:** Inserção no fim da lista encadeada em $O(n)$. Remoção percorrendo os nós em $O(n)$.

6. **Quick Sort**
   - **Utilização:** Ordenação principal para processamento e devolução do relatório "Top 5 Clientes".
   - **Complexidade:** $O(n \log n)$ no caso médio e $O(n^2)$ no pior caso.

7. **Recursão**
   - **Utilização:** Utilizada ativamente tanto no algoritmo de Quick Sort quanto no utilitário de filtragem por data do histórico.
   - **Complexidade:** No filtro, percorre linearmente todos os nós de forma recursiva operando em $O(n)$.