# Documento de modelos

## Modelo de dados

```mermaid
erDiagram
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
    boolean relizado
  }

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
