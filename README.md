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

## Setup

*1.* Clonar o repositório
```git clone git@github.com:marianaoliveira-mb/crypto-configs.git```

*2.* Criar uma virtual env
```python3 -m venv <NOME_DA_VIRTUAL_ENV>```

*3.* Ativar a virtual env
```source <NOME_DA_VIRTUAL_ENV>/bin/activate```

*4.* Instalar dependências
```pip install -r requirements.txt```

*5.* Preparar o DB
```python manage.py migrate```

*6.* Executar o servidor
```python manage.py runserver```

