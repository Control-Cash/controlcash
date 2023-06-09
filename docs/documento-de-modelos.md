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
    int vendedor FK "Usuario (id)"
    int cliente FK "Cliente (id)"
  }
  
  ItemVenda {
    int id PK
    int venda FK "Venda (id)"
    int produto FK "Produto (id)"
    int quantidade
    float valorUnidade
  } 

  Fornecedor {
    int id PK
    string nome
    string email
    int endereco FK "EnderecoFornecedor (id)"
  }

  TelefoneFornecedor {
    int id PK
    int telefone FK "Telefone (id)"
    int fornecedor FK "Fornecedor (id)"
  }

  EnderecoFornecedor {
    int endereco PK, FK "Endereco (id)"
    int fornecedor PK, FK "Fornecedor (id)"
  }

  Pedido {
    int id PK
    int quantidade
    int produto FK "Produto (id)"
    int usuario FK "Usuario (id)"
    int fornecedor FK "Fornecedor (id)"
    data data_entrega
    data data_pedido 
  }

  Produto {
    int id PK
    float precoVenda
    string nome
    string descricao
    int quantidadeEstoque
    date dataRegistro
  }

  CategoriaProduto {
    int produto PK, FK "Produto (id)"
    int categoria PK, FK "Categoria (id)"
  }

  Categoria {
    int id PK
    string nome
    boolean status
  }

  Cliente {
    int id PK
    string nome
    string email
    int EnderecoCliente FK "Endereco (IdEndereco)"
  }

  Telefone {
    int id PK
    string numero
    string tipo
  }

  TelefoneCliente {
    int id PK
    int telefone FK "Telefone (id)"
    int cliente FK "Cliente (id)"
  }

  TelefoneUsuario {
    int id PK
    int telefone FK "Telefone (id)"
    int usuario FK "Usuario (id)"
  }

  %% conexões
  Pagamento }o--|| FormaPagamento: ""
  FormaPagamento ||--o{ TaxaFormaPagamento: ""
  Taxa ||--o{ TaxaFormaPagamento: ""

  Pagamento }|--|| Venda: ""

  Venda }o--|| Cliente: ""

  Pedido ||--o{ Produto: ""
  Pedido ||--|| Usuario: ""
  Pedido ||--o{ Fornecedor: ""

  Fornecedor ||--|{ TelefoneFornecedor: ""
  Telefone ||--o{ TelefoneFornecedor: ""

  Fornecedor ||--|{ EnderecoFornecedor: ""
  Endereco ||--o{ EnderecoFornecedor: ""

  Usuario ||--|| Endereco : ""
  Cliente ||--|| Endereco : ""
  Venda ||--|{ ItemVenda : ""
  Produto ||--|| ItemVenda: ""
  Usuario ||--o{ Venda: ""

  CategoriaProduto }|--|| Produto: ""
  CategoriaProduto }o--|| Categoria: ""

  Cliente ||--o{ TelefoneCliente : ""
  Telefone ||--o{ TelefoneCliente : ""
  Usuario ||--o{ TelefoneUsuario : ""
  Telefone ||--o{ TelefoneUsuario : ""
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
