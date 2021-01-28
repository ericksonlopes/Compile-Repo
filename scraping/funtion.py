# importação de bibliotecas utilizadas
import requests
from bs4 import BeautifulSoup


def html_convert_python(url):
    """
        Função Converte o conteudo HTML recebido pela requisição em objetos python, Retornando esse obj
    :param url: -> url completa
    :return:
    """
    # Faz uma requisição trazendo o html
    req_get = requests.get(url)
    # beautifulSoup transforma um documento HTML complexo em uma árvore complexa de objetos Python.
    return BeautifulSoup(req_get.content, 'html.parser')  # retornando o obj
