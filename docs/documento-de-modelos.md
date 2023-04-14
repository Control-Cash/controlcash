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
