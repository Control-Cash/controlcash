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

#### RF01 - Manter usuário

Descrição: O sistema deve permitir o cadastro, listagem, visualização e edição
de novos usuários no sistema. Um usuário tem CPF, nome completo, email, data de
nascimento, endereço, salário, telefone, cargo, senha e status. Na listagem
apenas o CPF, nome completo, cargo e status são exibidos. Na visualização de
detalhes todos os atributos são exibidos, exceto senha. A edição de todos os
dados é permitida, mas para alteração de senha, salário ou status o gerente
deve fornecer sua própria senha para confirmar a ação.

Ator: Gerente

#### RF02 - Manter venda

Descrição:

Ator:

#### RF03 - Manter produto

Descrição:

Ator:

#### RF04 - Pesquisar produto

Descrição:

Ator:

#### RF05 - Manter item de venda

Descrição:

Ator:

#### RF06 - Manter pagamento de venda

Descrição:

Ator:

#### RF07 - Manter forma de pagamento

Descrição:

Ator:

#### RF08 - Manter prestação

Descrição: O Sistema deve permitir que os usuários do sistema insiram, atualizem
e consultem as informações de prestação de contas do caixa, incluindo o saldo inicial,
as entradas e saídas de dinheiro, o saldo final e o responsável pela movimentação do caixa.
Os usuários devem ser capazes de realizar essas ações de forma segura e protegida.
Além disso, a funcionalidade deve permitir a geração de relatórios de prestação de contas
para fins de auditoria e monitoramento. A precisão e integridade das informações de
prestação de contas devem ser mantidas em todos os momentos para garantir a confiabilidade
do sistema de controle de caixa.

Ator: Analista

#### RF09 - Manter cliente

Descrição:

Ator:

#### RF10 - Manter telefone

Descrição:

Ator:

#### RF11 - Manter endereço

Descrição:

Ator:

#### RF12 - Manter fornecedor

Descrição:

Ator:

#### RF13 - Manter pedido

Descrição:

Ator:

#### RF14 - Manter despesa

Descrição:

Ator:

#### RF15 - Manter categoria de produto

Descrição:

Ator:

#### RF16 - Relatar movimentação

Descrição: O sistema irá calcular o movimento de entrada e saída do caixa em um
intervalo de datas com base nas vendas, reposições de estoque, sálarios pagos
e despesas.

Ator: Gerente

#### RF17 - Relatar estoque baixo

Descrição: O sistema contará com um dashboard de estoque onde serão exibidos os
produtos com estoque baixo

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
