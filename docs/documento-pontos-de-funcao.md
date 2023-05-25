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


## US03 - Manter venda

| Descrição           | Tipo     |   RLR   |   DER   |   Complexidade   |   Tamanho em PF   |
| ------------------- | -------- | :-----: | :-----: | :--------------: | :---------------: |
| **Descrição**       | **Tipo** | **ALR** | **DER** | **Complexidade** | **Tamanho em PF** |
| Cadastrar venda     | EE       |    0    |    4    |      Baixa       |         3         |
| Editar venda        | EE       |    1    |    4    |      Baixa       |         3         |
| Listar venda        | SE       |    0    |    3    |      Baixa       |         4         |
| Visualizar venda    | SE       |    1    |    5    |      Baixa       |         4         |
| **Total**           |          |         |         |                  |        14         |

### Contagem Detalhada (Cd) do US02 - pesquisar produto 
|     Descrição      |   Tipo   |   ALR   |   DER   |   Complexidade   |   Tamanho em PF   |
| ------------------ | -------- | ------- | ------- | ---------------- | :---------------: |
|Digitar Nome/Código Do Produto|    EE    |    0    |    1    |      Baixa       | 3 PF              |
|  Exibir Lista de Produtos |    SE    |    0    |    3    |      Média       | 4 PF              |
|  Detalhar Produto  |    SE    |    0    |    4    |      Média       | 4 PF              |
|   **Total**        |          |         |         |           | **11 PF**         |
