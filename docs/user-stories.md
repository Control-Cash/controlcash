# Lista de User Stories

Este documento descreve os User Stories criados a partir da lista de requisitos
do [documento de visão](./documento-de-visao.md).

## US01 - Manter produto

Descrição: O sistema deve manter o cadastro dos produtos comercializados na
loja. Um produto tem código de identificação, nome, descrição, preço de venda e
quantidade em estoque. O usuário gerente terá acesso à criação e à edição de
produtos. Todos os usuários poderão visualizar a listagem e os dados dos
produtos.

| Requisitos envolvidos |                    |
| --------------------- | ------------------ |
| RF03                  | Cadastrar produto  |
| RF24                  | Listar produto     |
| RF25                  | Visualizar produto |
| RF26                  | Editar produto     |

|                    |           |
| ------------------ | --------- |
| Prioridade         | Essencial |
| Estimativa         | 8h        |
| Tempo gasto (real) | -         |
| Tamanho funcional  | -         |
| Analista           | Adriel    |
| Desenvolvedor      | -         |
| Revisor            | -         |
| Testador           | -         |

| Testes de aceitação (TA) |                                                  |
| ------------------------ | ------------------------------------------------ |
| Código                   | Descrição                                        |
| TA01.01                  | O usuário acessa a página de cadastro de produto, em seguida ele preenche os campos nome, descrição, preço de venda e quantidade em estoque e submete o formulário. O sistema salva o novo produto e redireciona o usuário para a página de listagem de produtos onde exibe a mensagem "Produto cadastrado com sucesso". |
| TA01.02                  | O usuário acessa a página de listagem de produtos e visualiza todos os produtos cadastrados no sistema, nessa tela o sistema exibe os campos nome, preço de venda e quantidade em estoque. |
| TA01.03                  | O usuário acessa a página de listagem de produtos e clica em um deles, em seguida o sistema o redireciona para a página de detalhes do produto, onde todas as informações, exceto código, são mostrados. |
| TA01.04                  | O usuário acessa a página de detalhes de um dos produtos e aperta no botão editar, em seguida o sistema o redireciona para uma tela onde há um formulário com todos os campos de produto, exceto código. Os campos já vem preenchidos com os valores atuais do produto. O usuário altera alguns desses campos com novas informações e submete o formulário. O sistema redireciona o usuário para a página de detalhes daquele produto onde a mensagem "Produto atualizado com sucesso" é exibida. |

## US02 - Pesquisar produto

Descrição: O sistema, deverar permitir pesquisar produtos no sistema pelo seu nome ou código para obter informações detalhadas sobre o produto, como preço, quantidade em estoque e categoria, para que possa selecionar o produto certo e realizar compras de forma eficiente.

| Requisitos envolvidos |                   |
| --------------------- | ----------------- |
| RF03                  | Manter produto    |
| RF04                  | Pesquisar produto |

|                    |     |
| ------------------ | --- |
| Prioridade         | Essencial    |
| Tempo gasto (real) |     |
| Tamanho funcional  |     |
| Analista           | Alef Luciano Silva    |
| Desenvolvedor      |     |
| Revisor            |     |
| Testador           |     |

| Testes de aceitação (TA) |           |
| ------------------------ | --------- |
| Código                   | Descrição |
| TA02.01                  | O usuário acessa a página de pesquisa de produto e digita o nome ou código do produto desajado. O sistema exibe uma lista com os produtos correspondente à pesquisa, contendo nome, preço de venda e quatidade em estoque. O usuário pode clicar em um dos produtos para ver mais informações sobre le na página de detalhes |

## US03 - Manter venda

Descrição:

| Requisitos envolvidos |     |
| --------------------- | --- |
|                       |     |

|                    |     |
| ------------------ | --- |
| Prioridade         |     |
| Tempo gasto (real) |     |
| Tamanho funcional  |     |
| Analista           |     |
| Desenvolvedor      |     |
| Revisor            |     |
| Testador           |     |

| Testes de aceitação (TA) |           |
| ------------------------ | --------- |
| Código                   | Descrição |
|                          |           |

## US04 - Manter item de venda

Descrição:

| Requisitos envolvidos |     |
| --------------------- | --- |
|                       |     |

|                    |     |
| ------------------ | --- |
| Prioridade         |     |
| Tempo gasto (real) |     |
| Tamanho funcional  |     |
| Analista           |     |
| Desenvolvedor      |     |
| Revisor            |     |
| Testador           |     |

| Testes de aceitação (TA) |           |
| ------------------------ | --------- |
| Código                   | Descrição |
|                          |           |

## US05 - Manter forma de pagamento

Descrição: O sistema deve ser capaz de gerenciar formas de pagamentos aceitas pelo comércio. Permitindo a inclusão, atualização e a remoção de tais formas de pagamento. Por exemplo pix, cartões de crédito e débito, boleto bancário, etc. Uma forma de pagamento deve possuir um id, nome e descrição e taxas(se houver). O responsável por realizar as operações deve ser o perfil administrador.

| Requisitos envolvidos |     |
| --------------------- | --- |
| RF02                  |     |
| RF06                  |     |

|                    |     |
| ------------------ | --- |
| Prioridade         |  essencial   |
| Tempo gasto (real) |  -   |
| Tamanho funcional  |  -   |
| Analista           | Guilherme Angelo de Medeiros |
| Desenvolvedor      |     |
| Revisor            |  -  |
| Testador           |  -  |

| Testes de aceitação (TA) |           |
| ------------------------ | --------- |
| Código                   | Descrição |
| TA05.01                         |  O perfil administrador financeiro acessa a página de formas de pagamento, ao clicar em "nova forma de pagamento", o administrador deverá preencher os campos refentes à forma de pagamento que ele deseja inserir, devendo preencher os campos nomes, descrição e caso haja taxas aplicáveis, elas também devem ser cadastradas no momento em que o administrador financeiro insere a nova forma de pagamento.          |
| TA05.02                         |  Posteriormente ao acréscimo de todos os dados necessários para inserção de uma nova forma de pagamento, em seus respectivos campos, o perfil administrador financeiro clica em "cadastrar". Ao fim do click, todos dados inseridos devem ser armazenados e persistidos no banco de dados, no qual as informações armazenadas devem se apresentar consistentes com as informações cadastradas pelo administrador. Após os dados serem armazenados, uma menssagem de confirmação de sucesso deve ser exibida com a seguite mensagem: "A nova forma de pagamento foi inserida com sucesso."      |
| TA05.03                         |  Posteriormente ao não preenchimento parcial ou não preenchimento total de todos os campos necessários para inserção de uma nova forma de pagamento, o perfil administrador financeiro clica em "cadastrar". Os campos totalmente não preenchidos ou parcialmente preenchidos não devem ser armazenados no banco de dados e a seguinte mensagem deve ser exibida: "Por favor, preencha todos os campos obrigatórios".           |
| TA05.04                         | O perfil administrador acessa a página "principal" (área restrita para administradores), ao clicar em pagamentos e acessar a página de formas de pagamento, devem ser listadas todas formas de pagamento já existentes. Caso nehuma forma de pagamento tenha sido cadastrada, deve ser exibida uma lista vazia com a seguinte mensagem: "Nenhuma forma de pagamento foi cadastrada".|
| TA05.05                         | O perfil administrador acessa a página "principal" (área restrita para administradores), ao clicar em pagamentos e acessar a página de formas de pagamento, o "usuário" clica em editar na forma de pagamento que deseja, ele deve ser redirecionado para uma página de edição de forma de pagamento. Ao realizar a modificação pretendida e clicar em salvar, os campos modificados devem ser atualizados e uma mensagem de sucesso deve ser exibida com o seguinte conteúdo: "Atualização realizada com sucesso."  |
| TA05.06                         | O perfil administrador acessa a página "principal" (área restrita para administradores), ao clicar em pagamentos e acessar a página de formas de pagamento, o "usuário" clica em editar na forma de pagamento que deseja, ele deve ser redirecionado para uma página de edição de forma de pagamento. Caso o "usuário" não faça nehuma alteração uma mensagem deve ser exibida: "Nenhuma modificação realizada."  |
| TA05.07                         | O perfil administrador acessa a página "principal" (área restrita para administradores), ao clicar em pagamentos e acessar a página de formas de pagamento, o "usuário" clica em editar na forma de pagamento que deseja, ele deve ser redirecionado para uma página de edição de forma de pagamento. Caso o "usuário" tente modificar um campo com um conteúdo nulo ou vazio, ao clicar em salvar, deve ser exibida a mensagem: Por favor, preencha o(s) campo(s) com informações válidas.  |
| TA05.08                         | O perfil administrador acessa a página "principal" (área restrita para administradores), ao clicar em pagamentos e acessar a página de formas de pagamento, o "usuário" clica em deletar na forma de pagamento que deseja. Ao confimar que deseja realmente excluir, a forma de pagamento deve ser removida do banco de dados.|


## US06 - Manter pagamento

Descrição: O sistema deve permitir a visualização da lista de pagamentos pendentes, recebidos e cancelados. Deve ser possível atualizar o status do pagamento de pendente para recebido ou cancelado, além de pesquisar pagamentos por data, valor ou id do cliente. Essas operações devem ser realizadas pelo perfil de administrador financeiro.

| Requisitos envolvidos |     |
| --------------------- | --- |
| RF06                  |     |
| RF30                  |     |

|                    |     |
| ------------------ | --- |
| Prioridade         | Essencial |
| Tempo gasto (real) |     |
| Tamanho funcional  |     |
| Analista           | Hilário |
| Desenvolvedor      |     |
| Revisor            |     |
| Testador           |     |

| Testes de aceitação (TA) |           |
| ------------------------ | --------- |
| Código                   | Descrição |
| TA06.01                  | O administrador financeiro acessa a página de pagamentos e em seguida seleciona a opção 'Visualizar pagamentos', onde será exibido um campo de filtro que permitirá que ele selecione entre as opções de pagamentos pendentes, recebidos ou cancelados. Em seguida, ele poderá visualizar a lista completa de pagamentos, com todas as informações relacionadas, de acordo com o filtro selecionado.|
| TA06.02                  | O administrador financeiro acessa a página de pagamentos e em seguida seleciona a opção 'Visualizar pagamentos'. Na página, é mostrado um filtro onde ele deverá selecionar a opção de pagamentos pendentes. Em seguida, ele deve selecionar um pagamento específico, onde serão exibidos todos os detalhes do pagamento, incluindo um botão para atualização do status. Ele pode mudar o status de pendente para cancelado ou recebido.|
| TA06.03                  | O administrador financeiro acessa a página de pagamentos e em seguida seleciona a opção 'Pesquisar pagamentos'. Na página, serão exibidos três campos para preenchimento: data, valor e cliente. Após preencher os campos, será mostrada uma lista de pagamentos de acordo com os critérios de pesquisa fornecidos. Caso o administrador deixe todos os campos em branco, o sistema não exibirá nenhum resultado de pesquisa.|

## US07 - Manter prestação

Descrição:

| Requisitos envolvidos |     |
| --------------------- | --- |
|                       |     |

|                    |     |
| ------------------ | --- |
| Prioridade         |     |
| Tempo gasto (real) |     |
| Tamanho funcional  |     |
| Analista           |     |
| Desenvolvedor      |     |
| Revisor            |     |
| Testador           |     |

| Testes de aceitação (TA) |           |
| ------------------------ | --------- |
| Código                   | Descrição |
|                          |           |

## US08 - Manter cliente

Descrição:

| Requisitos envolvidos |     |
| --------------------- | --- |
|                       |     |

|                    |     |
| ------------------ | --- |
| Prioridade         |     |
| Tempo gasto (real) |     |
| Tamanho funcional  |     |
| Analista           |     |
| Desenvolvedor      |     |
| Revisor            |     |
| Testador           |     |

| Testes de aceitação (TA) |           |
| ------------------------ | --------- |
| Código                   | Descrição |
|                          |           |

## US09 - Manter telefone

Descrição:

| Requisitos envolvidos |     |
| --------------------- | --- |
|                       |     |

|                    |     |
| ------------------ | --- |
| Prioridade         |     |
| Tempo gasto (real) |     |
| Tamanho funcional  |     |
| Analista           |     |
| Desenvolvedor      |     |
| Revisor            |     |
| Testador           |     |

| Testes de aceitação (TA) |           |
| ------------------------ | --------- |
| Código                   | Descrição |
|                          |           |

## US10 - Manter endereço

Descrição:

| Requisitos envolvidos |     |
| --------------------- | --- |
|                       |     |

|                    |     |
| ------------------ | --- |
| Prioridade         |     |
| Tempo gasto (real) |     |
| Tamanho funcional  |     |
| Analista           |     |
| Desenvolvedor      |     |
| Revisor            |     |
| Testador           |     |

| Testes de aceitação (TA) |           |
| ------------------------ | --------- |
| Código                   | Descrição |
|                          |           |

## US11 - Manter fornecedor

Descrição:

| Requisitos envolvidos |     |
| --------------------- | --- |
|                       |     |

|                    |     |
| ------------------ | --- |
| Prioridade         |     |
| Tempo gasto (real) |     |
| Tamanho funcional  |     |
| Analista           |     |
| Desenvolvedor      |     |
| Revisor            |     |
| Testador           |     |

| Testes de aceitação (TA) |           |
| ------------------------ | --------- |
| Código                   | Descrição |
|                          |           |

## US12 - Manter pedido

Descrição:

| Requisitos envolvidos |     |
| --------------------- | --- |
|                       |     |

|                    |     |
| ------------------ | --- |
| Prioridade         |     |
| Tempo gasto (real) |     |
| Tamanho funcional  |     |
| Analista           |     |
| Desenvolvedor      |     |
| Revisor            |     |
| Testador           |     |

| Testes de aceitação (TA) |           |
| ------------------------ | --------- |
| Código                   | Descrição |
|                          |           |

## US13 - Manter despesa

Descrição:

| Requisitos envolvidos |     |
| --------------------- | --- |
|                       |     |

|                    |     |
| ------------------ | --- |
| Prioridade         |     |
| Tempo gasto (real) |     |
| Tamanho funcional  |     |
| Analista           |     |
| Desenvolvedor      |     |
| Revisor            |     |
| Testador           |     |

| Testes de aceitação (TA) |           |
| ------------------------ | --------- |
| Código                   | Descrição |
|                          |           |

## US14 - Manter categoria de produto

Descrição:

| Requisitos envolvidos |     |
| --------------------- | --- |
|                       |     |

|                    |     |
| ------------------ | --- |
| Prioridade         |     |
| Tempo gasto (real) |     |
| Tamanho funcional  |     |
| Analista           |     |
| Desenvolvedor      |     |
| Revisor            |     |
| Testador           |     |

| Testes de aceitação (TA) |           |
| ------------------------ | --------- |
| Código                   | Descrição |
|                          |           |

## US15 - Gerar relatório de movimentação

Descrição:

| Requisitos envolvidos |     |
| --------------------- | --- |
|                       |     |

|                    |     |
| ------------------ | --- |
| Prioridade         |     |
| Tempo gasto (real) |     |
| Tamanho funcional  |     |
| Analista           |     |
| Desenvolvedor      |     |
| Revisor            |     |
| Testador           |     |

| Testes de aceitação (TA) |           |
| ------------------------ | --------- |
| Código                   | Descrição |
|                          |           |

## US16 - Gerar relatório de estoque

Descrição:

| Requisitos envolvidos |     |
| --------------------- | --- |
|                       |     |

|                    |     |
| ------------------ | --- |
| Prioridade         |     |
| Tempo gasto (real) |     |
| Tamanho funcional  |     |
| Analista           |     |
| Desenvolvedor      |     |
| Revisor            |     |
| Testador           |     |

| Testes de aceitação (TA) |           |
| ------------------------ | --------- |
| Código                   | Descrição |
|                          |           |

## US17 - Manter usuário

Descrição:

| Requisitos envolvidos |     |
| --------------------- | --- |
|                       |     |

|                    |     |
| ------------------ | --- |
| Prioridade         |     |
| Tempo gasto (real) |     |
| Tamanho funcional  |     |
| Analista           |     |
| Desenvolvedor      |     |
| Revisor            |     |
| Testador           |     |

| Testes de aceitação (TA) |           |
| ------------------------ | --------- |
| Código                   | Descrição |
|                          |           |
