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
  
  Endereco 
  {
    int IdEndereco PK
    string rua
    string bairro
    string cidade
    string estado
    string pais
    string cep
    string complemento
  }
  
  Usuario {
    int id PK
    string nome
    string senha
    date dataNascimento
    string email
    int tipoUsuario
    string urlFotoPerfil
    int EnderecoUsuario FK "Endereco (IdEndereco)"
  }
  
  Venda {
    int id PK
    date dataVenda
    float valorTotal
    id usuario FK "Usuario (id)"
  }
  
ItemVenda {
    int id PK
    int venda FK "Venda (id)"
    int produto FK "Produto (id)"
    int quantidade
    float valorUnidade
  } 

Fornecedor{
  int id PK
  string nome
  string email
  int endereco FK "EnderecoFornecedor (id)"
}

EnderecoFornecedor{
  int IdEndereco PK
  string rua
  string bairro
  string cidade
  string estado
  string pais
  string cep
  string complemento
}
  
  %% conexões
  Pagamento }o--|| FormaPagamento : ""
  FormaPagamento ||--o{ TaxaFormaPagamento : ""
  Taxa ||--o{ TaxaFormaPagamento : ""
  
   Usuario }|--|{ Endereco : ""
   Venda ||--|{ ItemVenda : ""
   Produto ||--|| ItemVenda: ""
   Usuario ||--o{ Venda: ""


  %% daqui até a linha com as três aspas são apenas exemplos, a pessoa que vai
  %% implementar essas tabelas pode excluir essas linhas para implementar sua
  %% própria versão
  Produto {
    int id PK
    int categoria FK
    float preco
  }

  CATEGORIA_PRODUTO {
    int produto PK, FK
    int categoria PK, FK
  }

  CATEGORIA {
    int id PK
    boolean status
  }

  Produto ||--o{ CATEGORIA_PRODUTO : ""
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

#### Tabela Pagamento

A tabela Pagamento guarda informações à respeito do pagamento de uma venda.

| Atributo | Descrição | Tamanho | Restrições de domínio |
| -------- | --------- | ------- | --------------------- |
| id       | Identificador unico do pagamento | - | Gerado automaticamente pelo banco de dados |
| pendente | Define se o pagamento já foi efetivado | - | O valor default é `true` |

#### Tabela FormaPagamento

A tabela FormaPagamento guarda informações à respeito das formas de pagamento
adotadas nas vendas.

| Atributo | Descrição | Tamanho | Restrições de domínio |
| -------- | --------- | ------- | --------------------- |
| id       | Identificador unico da forma de pagameto | - | Gerado automaticamente pelo banco de dados |
| descricao | Descreve em mais detalhes a forma de pagamento | 250 | Pode ser deixado em branco |

#### Tabela TaxaFormaPagamento

A tabela TaxaFormaPagamento guarda informações à respeito de cada taxa cobrada
em cada forma de pagamento.

| Atributo | Descrição | Tamanho | Restrições de domínio |
| -------- | --------- | ------- | --------------------- |
| id       | Identificador unico da taxa de forma de pagameto | - | Gerado automaticamente pelo banco de dados |

#### Tabela Taxa

A tabela Taxa guarda informações à respeito das taxas cobradas nas formas de
pagamento.

| Atributo | Descrição | Tamanho | Restrições de domínio |
| -------- | --------- | ------- | --------------------- |
| id       | Identificador unico da taxa | - | Gerado automaticamente pelo banco de dados |
| descricao | Descreve em mais detalhes a taxa | 250 | Pode ser deixado em branco |
| valor    | Descreve o valor da taxa | - | Não deve aceitar valor menor ou igual a zero |
| porcentagem | Define se o valor deve ser considerado como número absoluto ou porcentagem na hora de calcular a dedução de taxas | - | O valor default é `false` |
