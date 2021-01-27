from bs4 import BeautifulSoup
import requests


def get_directory_information(request_link, main):
    req_get = requests.get(request_link)
    dados = []
    soup = BeautifulSoup(req_get.content, 'html.parser')

    if main:
        classe = "Details-content--hidden-not-important js-navigation-container js-active-navigation-container " \
                 "d-md-block"
    else:
        classe = "Details-content--hidden-not-important js-navigation-container js-active-navigation-container " \
                 "d-block"

    for item in soup.find(class_=classe).find_all(role='row'):
        try:
            tag_link = item.find(class_='js-navigation-open link-gray-dark'), '\n'

            path = tag_link[0].attrs['href']
            name = path.split('/')[-1]
            extension = name.split('.')[-1]

            try:
                tipo = item.svg['aria-label']  # Directory
                if tipo != 'Directory':
                    tipo = 'File'
            except:
                tipo = 'File'

            objeto = {
                "nome": name,
                "path": path,
                "extension": extension,
                "tipo": tipo
            }

            dados.append(objeto)

        except:
            pass

    return dados


print(len(get_directory_information('https://github.com/Erickson-lopes-dev/SON-Advanced-Django', True)))
