# Compile Repo

[![Supported Python Versions](https://img.shields.io/pypi/pyversions/rich/10.11.0)](https://www.python.org/download/)
![Str](https://img.shields.io/github/stars/Erickson-lopes-dev/Compile-Repo?style=social) [![LinkedIn](https://img.shields.io/badge/LinkedIn-Erickson_Lopes%20-blue)](https://www.linkedin.com/in/ericksonlopes/)

Imagine uma API que liste para você todos os diretórios e arquivos com suas informações como.. path, tamanho, quantidade
de linhas...
Este é exatamente o propósito dessa API.

Basta realizar uma requisição via GET, um json com a chave igual a "repository" e o valor correspondente ao repositório (Usuario/Repositório)


- GET - https://compile-repo.herokuapp.com/repo

```json
// user/repository
{
  "repository": "Erickson-lopes-dev/Compile-Repo"
}
```

- Saída:

```json
{
  "branch": "master",
  "repository": "https://github.com/Erickson-lopes-dev/Compile-Repo",
  "directories": [
    {
      "link": "https://github.com/Erickson-lopes-dev/Compile-Repo/tree/master/tests",
      "name": "tests",
      "path": "/",
      "type": "Directory"
    },
    {
      ...
    }
  ],
  "files": [
    {
      "extension": "py",
      "lines": 19,
      "link": "https://github.com/Erickson-lopes-dev/Compile-Repo/blob/master/tests/test_compile_repo.py",
      "name": "test_compile_repo.py",
      "path": "/tests/",
      "size": "409 Bytes",
      "type": "File"
    },
    {
      ...
    }
  ]
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

## Exemplo de Funcionamento da Classe

```python
url = "Erickson-lopes-dev/Compile-Repo"
# Instância da classe
cr = CompileRepo(url)

print(cr.repository)  # Exibe o repositório
print(cr.files_list)  # Exibe a lista de arquivos
print(cr.directory_list)  # Exibe a lista de diretorios
print(cr.branch)  # Exibe branch do repo

# Recebe todos os dados obtidos da busca em um objeto
repo_data = cr.return_full_data_repo()

print(repo_data.repository)
print(repo_data.files)
print(repo_data.directories)
print(repo_data.branch)

```

## Deploy
![Heroku](https://img.shields.io/badge/-Heroku-430098?&logo=Heroku&logoColor=FFFFFF) 
![Gunicorn](https://img.shields.io/badge/-Gunicorn-499848?&logo=gunicorn&logoColor=FFFFFF)
