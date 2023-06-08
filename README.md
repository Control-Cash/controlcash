# ControlCash 💸

Sistema para controle de caixa e gerenciamento de estoque simplificado
desenvolvido usando Django.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)

## Documentação

Nessa seção você encontra a documentação usada para construir esse projeto.

[Documento de visão](./docs/documento-de-visao.md)

[Documento de modelos](./docs/documento-de-modelos.md)

[Documento de user stories](./docs/user-stories.md)

[Plano de releases](./docs/plano-releases.md)

[Plano de iterações](./docs/plano-iteracoes.md)

## Tutoriais

Esse projeto é construído usando o framework Django, a seguir você confere
alguns tutoriais que ensinam mais sobre essa tecnologia.

[Escrevendo seu primeiro app Django (Documentação oficial) - Artigos](https://docs.djangoproject.com/pt-br/4.0/intro/tutorial01/)

[Django 4 CRUD Completo em ~30 minutos (Canal Gregory Pacheco) - Vídeo](https://www.youtube.com/watch?v=GGBzMpIAgz4)

[Tutorial Django: Website da Biblioteca Local (MDN Docs) - Artigos](https://developer.mozilla.org/pt-BR/docs/Learn/Server-side/Django/Tutorial_local_library_website)

[Python Django Tutorial for Beginners (Canal Programming with Mosh) - Vídeo](https://www.youtube.com/watch?v=rHux0gMZ3Eg)

## Como executar o projeto

Para executar o projeto são necessários alguns requisitos.

1 - possuir o python instalado no computador.
2 - criar um ambiente virtal para instalar as dependências do projeto. Para isso execute o comando: python -m venv venv ou python3 -m venv venv.
3 - Precisamos ativar o venv para que as depedências sejam instaladas na pasta local do projeto. para isso basta executar o comando .\venv/Scripts/activate caso esteja no Windows ou source venv/bin/activate caso esteja no Minux ou no Mac.
3 - Agora precisamos instalar as dependências, para isso basta executar o seguinte comando. python -m pip install -r requirements.txt ou python3 -m pip install -r requirements.txt.
4 - feito isso precisamos entrar na pasta do projeto. Para isso use o comando: cd controlcash
5 - Feito o passo anterior agora precisamos fazer as migrações, use o comando: python manage.py makemigrations e posteriormente o comando: python manage.py migrate.
6 - Agora podemos executar o projeto, para isso execute o comando: python manage.py runserver e acesse o link que gera gerado.
7 - vá na url e coloque 127.0.0.1:8000/produto
8 - Pronto, agora poderá acessar o crud feito na iteração 2.