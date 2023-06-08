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
| **Total**           |          |         |         |                  |        27         |

### US02 - Pesquisar Produto 

|     Descrição      |   Tipo   |   ALR   |   DER   |   Complexidade   |   Tamanho em PF   |
| ------------------ | -------- | ------- | ------- | ---------------- | :---------------: |
|  Digitar Código    |    EE    |    0    |    1    |      Baixa       | 3 PF              |
|  Listar Produtos   |    SE    |    0    |    3    |      Baixa       | 4 PF              |
|  Detalhar Produto  |    SE    |    0    |    4    |      Baixa       | 4 PF              |
|   **Total**        |          |         |         |                  | **11 PF**         |

## US03 - Manter venda

| Descrição           | Tipo     |   RLR   |   DER   |   Complexidade   |   Tamanho em PF   |
| ------------------- | -------- | :-----: | :-----: | :--------------: | :---------------: |
| **Descrição**       | **Tipo** | **ALR** | **DER** | **Complexidade** | **Tamanho em PF** |
| Cadastrar venda     | EE       |    0    |    4    |      Baixa       |         3         |
| Editar venda        | EE       |    1    |    4    |      Baixa       |         3         |
| Listar venda        | SE       |    0    |    3    |      Baixa       |         4         |
| Visualizar venda    | SE       |    1    |    5    |      Baixa       |         4         |
| **Total**           |          |         |         |                  |        14         |

## US05 - Manter forma de pagamento

| Descrição           | Tipo     |   RLR   |   DER   |   Complexidade   |   Tamanho em PF   |
| ------------------- | -------- | :-----: | :-----: | :--------------: | :---------------: |
| forma de pagamento  | ALI      |    3    |    10   |      Baixa       |         7         |
|                     |          |         |         |                  |                   |
| **Descrição**                  | **Tipo** | **ALR** | **DER** | **Complexidade** | **Tamanho em PF** |
| Cadastrar forma de pagamento   | EE       |    0    |    3    |      Baixa       |         3         |
| Editar forma de pagamento      | EE       |    1    |    3    |      Baixa       |         3         |
| Listar forma de pagamento      | SE       |    0    |    3    |      Baixa       |         4         |
| Visualizar forma de pagamento  | SE       |    1    |    3    |      Baixa       |         4         |
|                                |          |         |         |                  |                   |
| **Total**                      |          |         |         |                  |        21         |