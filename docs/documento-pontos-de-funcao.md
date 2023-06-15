# Análise de pontos de função

## US01 - Manter produto

| Descrição           | Tipo     |   RLR   |   DER   |   Complexidade   |   Tamanho em PF   |
| ------------------- | -------- | :-----: | :-----: | :--------------: | :---------------: |
| Produto + Categoria | ALI      |    2    |    9    |      Baixa       |         7         |
|                     |          |         |         |                  |                   |
| **Descrição**       | **Tipo** | **ALR** | **DER** | **Complexidade** | **Tamanho em PF** |
| Cadastrar produto   | EE       |    0    |    4    |      Baixa       |         3         |
| Editar produto      | EE       |    1    |    5    |      Baixa       |         3         |
| Listar produtos     | SE       |    0    |    3    |      Baixa       |         4         |
| Visualizar produto  | SE       |    1    |    7    |      Baixa       |         4         |
|                     |          |         |         |                  |                   |
| **Total**           |          |         |         |                  |        14         |

### US02 - Pesquisar Produto

| Descrição        | Tipo | ALR | DER | Complexidade | Tamanho em PF |
| ---------------- | ---- | --- | --- | ------------ | :-----------: |
| Digitar Código   | EE   | 0   | 1   | Baixa        |     3 PF      |
| Listar Produtos  | SE   | 0   | 3   | Baixa        |     4 PF      |
| Detalhar Produto | SE   | 0   | 4   | Baixa        |     4 PF      |
| **Total**        |      |     |     |              |   **11 PF**   |

## US03 - Manter venda

| Descrição        | Tipo     |   RLR   |   DER   |   Complexidade   |   Tamanho em PF   |
| ---------------- | -------- | :-----: | :-----: | :--------------: | :---------------: |
| **Descrição**    | **Tipo** | **ALR** | **DER** | **Complexidade** | **Tamanho em PF** |
| Cadastrar venda  | EE       |    0    |    4    |      Baixa       |         3         |
| Editar venda     | EE       |    1    |    4    |      Baixa       |         3         |
| Listar venda     | SE       |    0    |    3    |      Baixa       |         4         |
| Visualizar venda | SE       |    1    |    5    |      Baixa       |         4         |
| **Total**        |          |         |         |                  |        14         |

## US08 - Manter cliente

| Descrição                     | Tipo     |   RLR   |   DER   |   Complexidade   |   Tamanho em PF   |
| ----------------------------- | -------- | :-----: | :-----: | :--------------: | :---------------: |
| Cliente + Endereco + Telefone | ALI      |    3    |   13    |      Baixa       |         7         |
|                               |          |         |         |                  |                   |
| **Descrição**                 | **Tipo** | **ALR** | **DER** | **Complexidade** | **Tamanho em PF** |
| Cadastrar cliente             | EE       |    0    |   10    |      Baixa       |         3         |
| Listar clientes               | SE       |    0    |    3    |      Baixa       |         4         |
| Visualizar cliente            | SE       |    0    |   10    |      Baixa       |         4         |
| Editar cliente                | EE       |    0    |   10    |      Baixa       |         3         |
| **Total**                     |          |         |         |                  |        14         |

## US13 - Manter despesa

| Descrição         | Tipo     |   RLR   |   DER   |   Complexidade   |   Tamanho em PF   |
| ----------------- | -------- | :-----: | :-----: | :--------------: | :---------------: |
| Despesa           | ALI      |    1    |    4    |      Baixa       |         7         |
|                   |          |         |         |                  |                   |
| **Descrição**     | **Tipo** | **ALR** | **DER** | **Complexidade** | **Tamanho em PF** |
| Cadastrar despesa | EE       |    0    |    3    |      Baixa       |         3         |
| Listar despesas   | SE       |    0    |    3    |      Baixa       |         4         |
| Editar despesa    | EE       |    0    |    3    |      Baixa       |         3         |
| Excluir despesa   | EE       |    0    |    0    |      Baixa       |         3         |
| **Total**         |          |         |         |                  |        13         |
