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
| Tamanho funcional  | [14](./documento-pontos-de-funcao.md#us01---manter-produto) |
| Analista           | Adriel    |
| Desenvolvedor      | Guilherme |
| Revisor            | Bianca    |
| Testador           | Hilário   |

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
| Estimativa         | 7h        |
| Tempo gasto (real) |     |
| Tamanho funcional  |     |
| Analista           | Alef Luciano Silva    |
| Desenvolvedor      |     |
| Revisor            |     |
| Testador           |     |

| Testes de aceitação (TA) |           |
| ------------------------ | --------- |
| Código                   | Descrição |
| TA02.01                  | O usuário acessa a página de pesquisa de produto e digita o nome ou código do produto desajado. O sistema exibe uma lista com os produtos correspondente à pesquisa, contendo nome, preço de venda e quatidade em estoque. O usuário pode clicar em um dos produtos para ver mais informações sobre ele na página de detalhes. |
| TA02.02                  | O usuário acessa a página de detalhes de um produto encontrado na pesquisa e verifica se todas as informações sobre o produto estão corretas, incluindo preço, quantidade em estoque e categoria. |

## US03 - Manter venda

Descrição: O sistema deve permitir o registro de  vendas. Uma venda contém os seguintes atributos: data, hora, cliente, itens de venda, valor total, pagamento, listagem, visualização de vendas e status.

| Requisitos envolvidos |     |
| --------------------- | --- |
| RF02                  | Manter venda    |

|                    |     |
| ------------------ | --- |
| Prioridade         | Essencial   |
| Estimativa         | 15h         |
| Tempo gasto (real) | 8h |
| Tamanho funcional  |     |
| Analista           | Bianca    |
| Desenvolvedor      | Adriel    |
| Revisor            | Guilherme |
| Testador           |     |

| Testes de aceitação (TA) |           |
| ------------------------ | --------- |
| Código                   | Descrição |
| TA03.01                  |Teste de cadastro de venda bem-sucedido: ao preencher todos os campos obrigatórios de uma nova venda e clicar no botão de cadastro, o sistema deve exibir uma mensagem de confirmação indicando que a venda foi registrada com sucesso.       |
| TA03.02                  |Teste de validação de campos obrigatórios: ao tentar cadastrar uma nova venda sem preencher algum dos campos obrigatórios, o sistema deve exibir uma mensagem de erro indicando quais campos estão faltando e impedir o cadastro da venda. |
| TA03.03                  |Teste de edição de venda: ao selecionar uma venda já registrada e clicar no botão de edição, o sistema deve permitir a alteração dos campos desejados e exibir uma mensagem de confirmação quando a venda for salva com sucesso.                |
| TA03.04                  |Teste de exclusão de venda: ao selecionar uma venda já registrada e clicar no botão de exclusão, o sistema deve exibir uma mensagem de confirmação e excluir a venda do sistema sem afetar outros dados do sistema.                             |

## US04 - Manter item de venda

Descrição: O sistema deverá permitir ao vendedor adicionar, editar ou remover um item de venda em uma venda. Cada item deve ter informações como produto, quantidade, e preço unitário.

| Requisitos envolvidos |                   |
| --------------------- | ----------------- |
| RF02                  | Manter venda      |
| RF03                  | Manter produto    |

|                    |                 |
| ------------------ | --------------- |
| Prioridade         | Média           |
| Tempo gasto (real) | 8h              |
| Tamanho funcional  | 17              |
| Analista           | Cíntia          |
| Desenvolvedor      | Adriel          |
| Revisor            | Bianca          |
| Testador           | -               |

| Testes de aceitação (TA) |                                                  |
| ------------------------ | ------------------------------------------------ |
| Código                   | Descrição                                        |
| TA04.01                  | O vendedor pode adicionar um item de venda com informações de produto, quantidade e preço unitário. |
| TA04.02                  | O vendedor pode editar as informações de um item de venda já existente, incluindo produto, quantidade e preço unitário. |
| TA04.03                  | O vendedor pode remover um item de venda existente. |
| TA04.04                  | O sistema verifica a disponibilidade em estoque do produto adicionado ou editado pelo vendedor. |
| TA04.05                  | O sistema atualiza o valor total da venda quando um ítem é adicionado ou editado. |

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

Descrição: O sistema deve permitir o gerenciamento de prestações de pagamentos realizadas pelos clientes. Isso inclui a possibilidade de criar, atualizar e remover prestações.

| Requisitos envolvidos |                           |
| --------------------- | ------------------------- |
| RF03                  | Manter venda              |
| RF05                  | Manter forma de pagamento |
| RF06                  | Manter pagamento          |

|                    |     |
| ------------------ | --- |
| Prioridade         |  Essencial   |
| Tempo gasto (real) |     |
| Tamanho funcional  |     |
| Analista           |     |
| Desenvolvedor      |     |
| Revisor            |     |
| Testador           |     |

| Testes de aceitação (TA) |           |
| ------------------------ | --------- |
| Código                   | Descrição |
| TA07.01                  | O administrador financeiro acessa a página de prestações e seleciona a opção "Visualizar prestações". Na página, é exibido um campo de filtro que permite selecionar entre as opções de prestações pendentes, pagas ou atrasadas |
| TA07.02                  |O administrador financeiro acessa a página de prestações e seleciona a opção "Visualizar prestações". Na página, é mostrado um filtro onde ele deve selecionar a opção de prestações pendentes. Em seguida, ele seleciona uma prestação específica, onde são exibidos todos os detalhes da prestação, incluindo um botão para atualizar o status.          |
| TA07.03                  | O administrador financeiro acessa a página de prestações e seleciona a opção "Pesquisar prestações". Na página, são exibidos três campos para preenchimento: data, valor e cliente. Após preencher os campos, é exibida uma lista de prestações de acordo com os critérios de pesquisa fornecidos.   |

## US08 - Manter cliente

Descrição: O sistema deve manter o cadastro dos clientes da loja. Um cliente tem
código de identificação, nome, telefone, endereço e email. Os usuários gerente
e vendedor terão acesso a edição e cadastro de clientes. Todos os usuários
poderão visualizar a listagem e os dados dos clientes.

| Requisitos envolvidos |      |
| --------------------- | ---- |
| Cadastrar cliente     | RF09 |
| Listar clientes       | RF34 |
| Visualizar cliente    | RF35 |
| Atualizar cliente     | RF36 |

|                    |     |
| ------------------ | --- |
| Prioridade         | Essencial |
| Tempo gasto (real) | 8h |
| Tamanho funcional  | [14](./documento-pontos-de-funcao.md#us08---manter-cliente) |
| Analista           | Adriel  |
| Desenvolvedor      | Adriel  |
| Revisor            | Bianca  |
| Testador           | Hilário |

| Testes de aceitação (TA) |           |
| ------------------------ | --------- |
| Código                   | Descrição |
| TA08.01 | O usuário acessa a página de cadastro de cliente, não preenche todos os campos obrigatórios do fomulário e tenta submeter o fomulário. O sistema não salva o cliente e informa na tela os campos que não foram preenchidos corretamente. |
| TA08.02 | O usuário acessa a página de cadastro de cliente, preenche todos os campos obrigatórios do fomulário e tenta submeter o fomulário. O sistema salva o novo cliente e redireciona o usuário para a página de visualização do cliente cadastrado. |
| TA08.03 | O usuário acessa a página de listagem de clientes e vê uma lista com todos os clientes cadastrados no sistema. Apenas o nome, telefone e email aparecem. |
| TA08.04 | O usuário acessa a página de detalhes de um cliente, lá é exibido todas as informações do cliente e um histórico de transações do cliente. |
| TA08.05 | O usuário acessa a página de edição de cliente, que contém um fomulário já preenchido com as informações salvas no banco de dados acerca daquele cliente. O usuário modifica alguns campos conforme necessário e submete o formulário. O sistema salva as alterações no banco de dados e redireciona o usuário para a página de visualização do cliente. |

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

Descrição: O sistema deve manter o cadastro das despesas da loja. Uma despesa
tem código de identificação, nome, valor, e um indicador para dizer se a depesa
é periódica. Os usuários gerente e administrador financeiro terão acesso a
criação, edição, listagem e exclusão das despesas.

| Requisitos envolvidos |      |
| --------------------- | ---- |
| Cadastrar despesa     | RF14 |
| Listar despesas       | RF50 |
| Editar despesa        | RF51 |
| Excluir despesa       | RF52 |

|                    |     |
| ------------------ | --- |
| Prioridade         | Desejável |
| Tempo estimado | 8h |
| Tempo gasto (real) | - |
| Tamanho funcional  | [13](./documento-pontos-de-funcao.md#us13---manter-despesa) |
| Analista           | Adriel |
| Desenvolvedor      | Adriel |
| Revisor            | Hilário |
| Testador           | Guilherme |

| Testes de aceitação (TA) |           |
| ------------------------ | --------- |
| Código | Descrição |
| TA13.01 | O usuário acessa a tela de cadastro de despesa, onde preenche um fomulário com os campos nome, valor e despesa periódica. O usuário submete o formulário e o sistema realiza salva a despesa no banco de dados. Em seguida o sistema redireciona o usuário para a página de listagem. |
| TA13.02 | O usuário acessa a tela de cadastro de despesa, preenche apenas parte dos campos e tenta submeter o formulário, o sistema não salva a nova despesa e informa ao usuário os problemas com o formulário. |
| TA13.03 | O usuário acessa a tela de listagem de despesas e visualiza todas as despesas cadastradas no sistema. |
| TA13.04 | O usuário acessa a tela de edição de despesa onde é exibido um formulário já preenchido com os dados presentes no banco de dados. O usuário modifica alguns desses dados e submete o formulário. O sistema salva as alterações e redireciona o usuário para a listagem de despesas. |
| TA13.05 | O usuário tenta excluir uma despesa clicando no botão apagar. O sistema direciona o usuário para uma página de confirmação, lá o usuário confirma a exclusão e é redirecionado para a página de listagem de despesas. |

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
