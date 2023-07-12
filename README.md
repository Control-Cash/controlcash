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

Você pode executar o projeto utilizando o mariadb através do docker ou usar o
SQLite3 padrão do django.

- [Tutorial com o SQLite](#com-o-sqlite)

- [Tutorial com docker e mariadb](#com-o-mariadb-via-docker)

### Com o SQLite


1. Possuir o [python](https://www.python.org/) 3.9 ou superior instalado no
  computador.

2. Criar um ambiente virtual para instalar as dependências do projeto. Para
  isso execute um dos comandos a seguir

   ```powershell
   python -m venv venv
   ```

   ou

   ```bash
   python3 -m venv venv
   ```

3. Precisamos ativar o venv para que as depedências sejam instaladas na pasta
  local do projeto. Para isso basta executar um dos comandos a seguir.

   - Windows

     ```powershell
     .\venv/Scripts/activate
     ```

   - Linux/Mac

     ```bash
     source venv/bin/activate
     ```

4. Agora precisamos instalar as dependências, para isso basta executar o
  seguinte comando

   - Windows

     ```powershell
     python -m pip install -r requirements.txt
     ```

   - Linux/Mac

     ```bash
     python3 -m pip install -r requirements.txt
     ```

5. Feito isso, precisamos entrar na pasta do projeto

   ```bash
   cd controlcash
   ```

6. Copie o arquivo `.env.example` e o renomeie para `.env`

   - Linux

     ```bash
     cp .env.example .env
     ```
  
   - Windows

     ```powershell
     copy .env.example .env
     ```

7. Feito o passo anterior, agora precisamos fazer as migrações usando os
   comandos a seguir

   ```bash
   python manage.py makemigrations
   ```

   ```bash
   python manage.py migrate
   ```

8. Agora podemos executar o projeto

   ```bash
   python manage.py runserver
   ```

9. Agora acesse a URL mostrada no terminal:
   - [http://localhost:8000/produto](http://localhost:8000/produto)

### Com o MariaDB via Docker

1. Possuir o [python](https://www.python.org/) 3.9 ou superior instalado no
  computador.

2. Criar um ambiente virtual para instalar as dependências do projeto. Para
  isso execute um dos comandos a seguir

   ```powershell
   python -m venv venv
   ```

   ou

   ```bash
   python3 -m venv venv
   ```

3. Precisamos ativar o venv para que as depedências sejam instaladas na pasta
  local do projeto. Para isso basta executar um dos comandos a seguir.

   - Windows

     ```powershell
     .\venv/Scripts/activate
     ```

   - Linux/Mac

     ```bash
     source venv/bin/activate
     ```

4. Agora precisamos instalar as dependências, para isso basta executar o
  seguinte comando

   - Windows

     ```powershell
     python -m pip install -r requirements.txt
     ```

   - Linux/Mac

     ```bash
     python3 -m pip install -r requirements.txt
     ```

5. Feito isso, precisamos entrar na pasta do projeto

   ```bash
   cd controlcash
   ```

6. Copie o arquivo `.env.example` e o renomeie para `.env`

   - Linux

     ```bash
     cp .env.example .env
     ```
  
   - Windows

     ```powershell
     copy .env.example .env
     ```

7. Crie um diretorio para o volume do container com o MariaDB

   ```bash
   mkdir -p $HOME/docker/volumes/controlcash-db
   ```

8. Inicie um container docker com o MariaDB

   - Lembre-se de alterar o valor da variável `MARIADB_ROOT_PASSWORD` para a
   senha que deseja utilizar em seu banco

     ```bash
     docker run --name mariadb-controlcash -v $HOME/docker/volumes/controlcash-db:/var/lib/mysql -e MARIADB_ROOT_PASSWORD=controlcash -d -p 3306:3306 mariadb:latest
     ```

9. Acesse o MariaDB via terminal com o comando abaixo, ele solicitará a senha
que você definiu no passo anterior

   ```bash
   docker exec -it mariadb-controlcash mariadb --user root -p
   ```

10. Crie um banco de dados para a aplicação

    ```sql
    create database controlcash;
    ```

11. Saia do terminal do MariaDB com o comando `exit`, e abra o arquivo `.env` no
seu editor de código favorito.

12. Preencha o arquivo `.env` com os dados do banco de dados que você acabou de
criar, e altere a variável `USE_SQLITE` para `False`.

13. Feito o passo anterior, agora precisamos fazer as migrações usando os
   comandos a seguir

    ```bash
    python manage.py makemigrations
    ```

    ```bash
    python manage.py migrate
    ```

14. Agora podemos executar o projeto

    ```bash
    python manage.py runserver
    ```

15. Agora acesse a URL para a página de produtos:
  
    - [http://localhost/produto](http://localhost/produto)

## Em caso de erro

### Ao instalar os pacotes com o pip

Instale os pacotes a seguir no linux

```bash
sudo apt update

sudo apt install libmariadb-dev python3-dev default-libmysqlclient-dev build-essential
```

### Ao tentar executar a aplicação

No arquivo `ControlCash/settings.py`, verifique se a configuração do banco de
dados está com `HOST` igual a `localhost`, caso esteja, troque para `127.0.0.1`.

- Deve estar parecido com isso:

  ```python
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': 'controlcash',
          'USER': 'controlcash',
          'PASSWORD': 'controlcash',
          'HOST': '127.0.0.1',
          'PORT': 3306
      }
  }
  ```
