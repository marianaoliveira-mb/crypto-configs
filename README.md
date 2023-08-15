# Cripto-configs

O objetivo desse projeto é construir uma aplicação para o cadastro de cryptomoedas com suas cotações atuais e listar estas informações.

## Pré-requisitos

- Python
- Django
- Docker
- PostgreSQL
- Git/GitHub

## Instalação

- Python: No Windows https://python.org.br/instalacao-windows/
          No Linux https://python.org.br/instalacao-linux/

- Django: https://www.djangoproject.com/download/

- Docker: https://docs.docker.com/get-docker/

- ProstgreSQL: https://www.postgresql.org/download/

- Git: https://learn.microsoft.com/pt-br/devops/develop/git/install-and-set-up-git

## Passo a passo

*1.* Criar novo diretório 
```mkdir desafio2``

*2.* Criar venv
- Para criar o ambiente virtual:
```python3 -m venv venv```
- Ativar o ambiente virtual:
```source venv/bin/activate```

*3.* Iniciar projeto django
- Criar o esqueleto do "config"
```django-admin startproject config .```
- Executar as migrações do bd:
```python manage.py migrate```
- Rodar o web server usando:
```python3 manage.py runserver```

*4.* Criar app cryptoConfigs
- Criar app:
```django-admin startapp cryptoConfigs```
    
*5.* Criar view post para salvar dados do ativo
- Criar uma view para receber a requisição do front e, se o método da requisição for um POST, ele pega os itens crypto e armazena no banco de dados.

*6.* Criar view para listar todos os registros de um ativo
- Criar uma view para retornar todos os dados da tabela crypto em um formato de lista

*7.* Criar tabela (no Django chamada model)
- Criar tabela dentro do app(cryptoConfigs) no arquivo models.py:/

*8.* Rodar migrations
- Fazendo as migrações da app:
```python manage.py makemigrations```
```python manage.py migrate```
	
*9.* Subir postgres em container
- Criar o arquivo docker-compose.yml
- Modificar o arquivo settings.py para guardar os dados da aplicação em postgres e não em SqlLite
- Subir o docker com: 
```docker-compose up -d```
- Fazer as migrações do bd com: 
```python manage.py migrate```
- E rodar a aplicação usando: 
```python manage.py runserver```

