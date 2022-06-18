# Compile Repo

[![Supported Python Versions](https://img.shields.io/pypi/pyversions/rich/10.11.0)](https://www.python.org/download/)
![Str](https://img.shields.io/github/stars/Erickson-lopes-dev/Compile-Repo?style=social) [![LinkedIn](https://img.shields.io/badge/LinkedIn-Erickson_Lopes%20-blue)](https://www.linkedin.com/in/ericksonlopes/)

Imagine uma API que te liste todos os diretórios e arquivos com suas informações como. path, tamanho, quantidade de
linhas... Este é exatamente o propósito dessa API.

Basta realizar uma requisição via GET, um json com a chave igual a "repository" e o valor correspondente ao
repositório (Usuário/Repositório)

# Documentação

- Files and directories

> POST - https://compile-repo.herokuapp.com/repofd

```json
{
  "repository": "Erickson-lopes-dev/Compile-Repo",
  "branch": "master"
}
```

- Branchs

> POST - https://compile-repo.herokuapp.com/branchs

```json
{
  "repository": "Erickson-lopes-dev/Compile-Repo"
}
```

- Releases

> POST - https://compile-repo.herokuapp.com/releases

```json
{
  "repository": "Erickson-lopes-dev/Compile-Repo"
}
```

## Instalação

No cmd:

```commandline
git clone https://github.com/Erickson-lopes-dev/Compile-Repo
cd Compile-Repo
pip install -r requirements.txt

python app.run
```

## Deploy

![Heroku](https://img.shields.io/badge/-Heroku-430098?&logo=Heroku&logoColor=FFFFFF)
![Gunicorn](https://img.shields.io/badge/-Gunicorn-499848?&logo=gunicorn&logoColor=FFFFFF)
![Flask](https://img.shields.io/badge/-Flask-181717?&logo=Flask&logoColor=FFFFFF) 
