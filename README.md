# <h1>Compile-Repo</h1>
<p>O projeto em si procura todos os arquivos em cada repositório indicado e exibe cada um deles em uma tabela onde se é apresentado o  caminho, nome do arquivo, extensão, quantidade de linhas e tamanho do arquivo.</p>

<p>A versão utilizada para desenvolvimento foi Python 3.6.4, porém qualquer versão do python 3 pode ser utilizada.</p>


## Instalação

Instalar [Python 3](https://www.python.org/download/).

No cmd:
```
git clone https://github.com/Erickson-lopes-dev/Compile-Repo
cd Compile-Repo
pip install -r requeriments.txt
```

## Exemplo

Insira dentro do arquivo 'repositories.txt' os repositórios que deseja analisar:
```
Erickson-lopes-dev/Compile-Repo
jazzband/prettytable
tqdm/tqdm
psf/requests
```

Em seguida execute o arquivo main:
```
py main.py
```

Resultado: 
![image](https://user-images.githubusercontent.com/62525983/106611192-6d40a000-6546-11eb-952e-7cca893bfaa6.png)

