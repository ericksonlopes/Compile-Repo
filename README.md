# Compile Repo

[![Supported Python Versions](https://img.shields.io/pypi/pyversions/rich/10.11.0)](https://www.python.org/download/)
![Str](https://img.shields.io/github/stars/Erickson-lopes-dev/Compile-Repo?style=social) [![LinkedIn](https://img.shields.io/badge/LinkedIn-Erickson_Lopes%20-blue)](https://www.linkedin.com/in/ericksonlopes/)

O projeto em si procura todos os arquivos em cada repositório indicado e exibe cada um deles em uma tabela onde se é
apresentado o caminho, nome do arquivo, extensão, quantidade de linhas e tamanho do arquivo.

## Instalação

No cmd:

```
git clone https://github.com/Erickson-lopes-dev/Compile-Repo
cd Compile-Repo
pip install -r requirements.txt
```

## Exemplo de Funcionamento da Classe

Insira dentro do arquivo 'repositories.txt' os repositórios que deseja analisar:

Em seguida execute o arquivo main:

```python
# Instância da classe
cr = CompileRepo(url)

# Executa o código de busca
cr.get_diretories_and_files()

# Armazena os arquivos
list_files = cr.files_list
print(list_files, '\n')

# Armazena os diretórios
list_directories = cr.directory_list
print(list_directories, '\n')
```