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

6. Feito o passo anterior, agora precisamos fazer as migrações usando os
   comandos a seguir

   ```bash
   python manage.py makemigrations
   ```

   ```bash
   python manage.py migrate
   ```

7. Agora podemos executar o projeto

   ```bash
   python manage.py runserver
   ```

8. Agora acesse a URL mostrada no terminal:
   - [http://localhost:8000/produto](http://localhost:8000/produto)

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
