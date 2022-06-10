# Compile Repo

[![Supported Python Versions](https://img.shields.io/pypi/pyversions/rich/10.11.0)](https://www.python.org/download/)
![Str](https://img.shields.io/github/stars/Erickson-lopes-dev/Compile-Repo?style=social) [![LinkedIn](https://img.shields.io/badge/LinkedIn-Erickson_Lopes%20-blue)](https://www.linkedin.com/in/ericksonlopes/)

Imagine uma API que liste para você todos os diretórios e arquivos ()

- Envie na url https://compile-repo.herokuapp.com/

```json
{
  "repository": "Erickson-lopes-dev/Compile-Repo"
}
```

- A saída será:

```json
{
  "directories": [
    {
      "link": "https://github.com/Erickson-lopes-dev/Compile-Repo/tree/master/tests",
      "name": "tests",
      "type": "Directory"
    },
    {
      ...
    }
  ],
  "files": [
    {
      "extension": "gitignore",
      "lines": 131,
      "link": "https://github.com/Erickson-lopes-dev/Compile-Repo/blob/master/.gitignore",
      "name": ".gitignore",
      "size": "1.78 KB",
      "type": "File"
    },
    {
      ...
    }
  ],
  "repository": "https://github.com/Erickson-lopes-dev/Compile-Repo"
}
```

## Instalação

No cmd:

```commandline
git clone https://github.com/Erickson-lopes-dev/Compile-Repo
cd Compile-Repo
pip install -r requirements.txt
```

## Exemplo de Funcionamento da Classe

```python
# Instância da classe
cr = CompileRepo(url)

# Executa o código de busca
cr.get_diretories_and_files()

print(cr.repository)  # exibe o repositório
print(cr.files_list)  # exibe a lista de arquivos
print(cr.directory_list)  # exibe a lista de diretorios

# Recebe todos os dados obtidos da busca em um objeto
repo_data = cr.return_full_data_repo()

print(repo_data.repository)
print(repo_data.files)
print(repo_data.directories)
```