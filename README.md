# <h1>Compile-Repo</h1>
<p>O projeto em si procura todos os arquivos em cada repositório indicado e exibe cada um deles em uma tabela onde se é apresentado o  caminho, nome do arquivo, extensão, quantidade de linhas e tamanho do arquivo.</p>

<p>A versão utilizada para desenvolvimento foi Python 3.6.4, porém qualquer versão do python 3 pode ser utilizada.</p>


## Instalação

Instalar [Python 3](https://www.python.org/download/).

No cmd:
```
git clone https://github.com/Erickson-lopes-dev/Compile-Repo
cd Compile-Repo
pip install -r requirements.txt
```

## Exemplo de Funcionamento

Insira dentro do arquivo 'repositories.txt' os repositórios que deseja analisar:


Em seguida execute o arquivo main:
```python
cr = CompileRepo(url)

# Executa o código de busca
cr.get_infos()

list_files = cr.files_list
print(list_files, '\n')

list_directories = cr.directory_list
print(list_directories, '\n')
```

Resultado: 
![image](https://user-images.githubusercontent.com/62525983/106611192-6d40a000-6546-11eb-952e-7cca893bfaa6.png)

