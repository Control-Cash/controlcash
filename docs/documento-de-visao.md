# Documento de visão

## Equipe e definição de papéis

| Membro                              | Papel             | Email                           |
| ----------------------------------- | ----------------- | ------------------------------- |
| Adriel Faria dos Santos             | Gerente, Analista | adriel.fsantos@outlook.com      |
| Alef Luciano Silva                  | Analista          | alef.silva.123@ufrn.edu.br      |
| Bianca Laise Medeiros Cassiano      | Analista          | bianca.medeiros.098@ufrn.edu.br |
| Cintia Campos de Queiroz            | Analista          | cintia.campos.109@ufrn.edu.br   |
| Guilherme Angelo de Medeiros        | Analista          | guilhermeangelo2001@gmail.com   |
| Hilário Petronio de Medeiros Dantas | Analista          | hilariod94@gmail.com            |

## Matriz de copetências

| Membro    | Competências                                                 |
| --------- | ------------------------------------------------------------ |
| Adriel    | Typescript, Javascript, Python, HTML, CSS, Git, SQL, MongoDB |
| Alef      | JavaScript, HTML, CSS, Python, SQL, C                        |
| Bianca    | JavaScript, HTML, CSS, Python, SQL, C++, C                   |
| Cintia    | Comunicação, Proatividade, Liderança                         |
| Guilherme | Python, HTML, Javascript, Git                                |
| Hilário   | Python, HTML, Javascript, Git                                |

## Descrição do projeto

A necessidade do sistema de controle de caixa surgiu com o aumento do fluxo de
vendas de um comércio. O projeto tem como ideal facilitar a logística de entrada
e saída monetária da empresa comercial em questão, bem como o monitoramento de
forma simplificada do estoque, promovendo uma melhoria da eficiência
operacional e do controle das operações financeiras.

### Perfis dos usuários

O sistema poderá ser utilizado por dois tipos de usuário.

#### Perfil Gerente

Este usuário tem permissão a todas as áreas do sistema.

#### Perfil Vendedor

Este usuário terá acesso ao controle de venda, controle de pagamentos,
controle de prestações pendentes, formas de pagamento, e gestão de clientes.

### Requisitos funcionais

#### RF01 - Cadastrar usuário

Descrição: O sistema permite a inserção de novos usuários no sistema. Um usuário
tem os atributos CPF, nome completo, email, data de nascimento, endereço,
salário, telefone, cargo, senha e status.

Ator: Gerente

#### RF02 - Listar usuários

Descrição: Os usuários cadastrados no sistema podem ser listados. Nessa forma de
visualização apenas o CPF, nome completo, cargo e status são exibidos.

Ator: Gerente

#### RF03 - Visualizar detalhes de usuário

Descrição: Os dados de um usuário cadastrado no sistema podem ser visualizado.
Nessa forma de visualização todos os atributos são exibidos, exceto senha.

Ator: Gerente

#### RF04 - Editar usuário

Descrição: Os dados de um usuário cadastrado no sistema podem ser editados.
Todos os atributos são editáveis. Para alteração de senha ou status o gerente
deve fornecer sua própria senha para confirmar a ação.

Ator: Gerente

#### RF05 - Cadastrar venda

Descrição:

Ator:

#### RF06 - Listar vendas

Descrição:

Ator:

#### RF07 - Editar venda

Descrição:

Ator:

#### RF08 - Desativar venda

Descrição:

Ator:

#### RF09 - Cadastrar Produto

Descrição:

Ator:

#### RF10 - Listar produtos

Descrição:

Ator:

#### RF11 - Pesquisar produto

Descrição:

Ator:

#### RF12 - Editar produto

Descrição:

Ator:

#### RF13 - Cadastrar item de venda

Descrição:

Ator:

#### RF14 - Listar itens de venda

Descrição:

Ator:

#### RF15 - Editar item de venda

Descrição:

Ator:

#### RF16 - Remover item de venda

Descrição:

Ator:

#### RF17 - Cadastrar pagamento de venda

Descrição:

Ator:

#### RF18 - Exibir detalhes de pagamento de venda

Descrição:

Ator:

#### RF19 - Editar pagamento de venda

Descrição:

Ator:

#### RF20 - Remover pagamento de venda

Descrição:

Ator:

#### RF21 - Cadastrar forma de pagamento

Descrição:

Ator:

#### RF22 - Listar formas de pagamento

Descrição:

Ator:

#### RF23 - Editar forma de pagamento

Descrição:

Ator:

#### RF24 - Desativar forma de pagamento

Descrição:

Ator:

#### RF25 - Cadastrar prestação

Descrição:

Ator:

#### RF26 - Ver detalhes de prestação

Descrição:

Ator:

#### RF27 - Cadastrar cliente

Descrição:

Ator:

#### RF28 - Listar clientes

Descrição:

Ator:

#### RF29 - Ver detalhes de cliente

Descrição:

Ator:

#### RF30 - Editar cliente

Descrição:

Ator:

#### RF31 - Cadastrar telefone

Descrição:

Ator:

#### RF32 - Editar telefone

Descrição:

Ator:

#### RF33 - Remover telefone

Descrição:

Ator:

#### RF34 - Cadastrar endereço

Descrição:

Ator:

#### RF35 - Editar endereço

Descrição:

Ator:

#### RF36 - Remover endereço

Descrição:

Ator:

#### RF37 - Cadastrar fornecedor

Descrição:

Ator:

#### RF38 - Listar fornecedores

Descrição:

Ator:

#### RF39 - Editar fornecedor

Descrição:

Ator:

#### RF40 - Exibir detalhes de fornecedor

Descrição:

Ator:

#### RF41 - Cadastrar pedido

Descrição:

Ator:

#### RF42 - Listar pedidos

Descrição:

Ator:

#### RF43 - Exibir detalhes de pedido

Descrição:

Ator:

#### RF44 - Remover pedido

Descrição:

Ator:

#### RF45 - Cadastrar despesa

Descrição:

Ator:

#### RF46 - Listar depesas

Descrição:

Ator:

#### RF47 - Exibir detalhes de despesa

Descrição:

Ator:

#### RF48 - Editar despesa

Descrição:

Ator:

#### RF49 - Desativar despesa

Descrição:

Ator:

#### RF50 - Cadastrar categoria de produto

Descrição:

Ator:

#### RF51 - Listar categorias de produto

Descrição:

Ator:

#### RF52 - Editar categoria de produto

Descrição:

Ator:

#### RF53 - Desativar categoria de produto

Descrição:

Ator:

#### RF54 - Relatar movimentação

Descrição: O sistema irá calcular o movimento de entrada e saída do caixa em um
intervalo de datas com base nas vendas, reposições de estoque, sálarios pagos
e despesas.

Ator: Gerente

### Requisitos não funcionais

| Código | Descrição                                                              |
| ------ | ---------------------------------------------------------------------- |
| RNF01  | Usuários com menos privilégios de acesso, tem ação limitada no sistema |
| RNF02  | O sistema deve ter boa experiência de uso                              |
| RNF03  | O sistema deve ser responsivo                                          |
| RNF04  | As senhas dos usuários devem ser armazenadas de forma criptografada    |
| RNF05  | O sistema sempre deve ter no mínimo um gerente ativo                   |
| RNF06  | O sistema deve ser acessível pelos navegadores Chrome e Firefox        |

### Riscos

| Data       | Risco                                  | Prioridade | Responsável | Status  | Providência/Solução    |
| ---------- | -------------------------------------- | ---------- | ----------- | ------- | ---------------------- |
| 02/04/2023 | Não aprendizado do framework escolhido | Alta       | Gerente     | Vigente | Reforço de estudos     |
| 02/04/2023 | Inconsistência entre requisitos        | Alta       | Todos       | Vigente | Reunião de alinhamento |
| 02/04/2023 | Má divisão de tarefas                  | Média      | Gerente     | Vigente | Redivisão de tarefas   |
| 02/04/2023 | Atraso de cronograma                   | Baixa      | Gerente     | Vigente | Reoganização de equipe |

## Referências

[Modelo de documento de visão do BSI](https://docs.google.com/document/d/1DPBcyGHgflmz5RDsZQ2X8KVBPoEF5PdAz9BBNFyLa6A/edit)
