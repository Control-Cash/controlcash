# Documento de modelos

## Modelo de dados

```mermaid
erDiagram
  %% tabelas
  Despesa {
    int id PK
    string nome
    float valor
    boolean periodica
  }

  Pagamento {
    int id PK
    int tipo FK "FormaPagamento (id)"
    int venda FK "Venda (id)"
    boolean pendente
  }

  FormaPagamento {
    int id PK
    string nome
    string descricao
  }

  TaxaFormaPagamento {
    int id PK
    int formaPagamento FK "FormaPagamento (id)"
    int taxa FK "Taxa (id)"
  }

  Taxa {
    int id PK
    stirng nome
    string descricao
    float valor
    boolean porcentagem
  }

  %% conexões
  Pagamento }o--|| FormaPagamento : ""
  FormaPagamento ||--o{ TaxaFormaPagamento : ""
  Taxa ||--o{ TaxaFormaPagamento : ""



  %% daqui até a linha com as três aspas são apenas exemplos, a pessoa que vai
  %% implementar essas tabelas pode excluir essas linhas para implementar sua
  %% própria versão
  PRODUTO {
    int id PK
    int categoria FK
  }

  CATEGORIA_PRODUTO {
    int produto PK, FK
    int categoria PK, FK
  }

  CATEGORIA {
    int id PK
    boolean status
  }

  PRODUTO ||--o{ CATEGORIA_PRODUTO : ""
  CATEGORIA ||--o{ CATEGORIA_PRODUTO : ""
```

### Dicionário de dados

#### Tabela Despesa

A tabela despesa guarda informações à respeito das contas que a empresa deve
pagar.

| Atributo | Descrição | Tamanho | Restrições |
| -------- | --------- | ------- | ---------- |
| id       | Identificador unico da despesa | - | Gerado automaticamente pelo banco de dados |
| nome     | Descreve o nome da despesa | 150 | - |
| periodica | Define se aquela despesa se repete mensalmente | - | O valor default é `false` |
| valor    | Descreve o valor da despesa | - | Não deve aceitar valor menor ou igual a zero |
