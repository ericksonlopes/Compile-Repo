from scraping.funtion import html_convert_python


def get_lines_bytes(url):
    # converte
    obj_soup = html_convert_python(url)
    # busca o texto
    infos = obj_soup.find(class_='text-mono f6 flex-auto pr-3 flex-order-2 flex-md-order-1 mt-2 mt-md-0').text

    formated = infos.replace('symbolic link', '').replace('executable file', '').split()

    # se o a str for um formato padrão -> {'lines': 10, 'KB': '10'}
    if len(formated) == 6:

        # info: Fazer-> Converter tudo para bytes #
        # retorna um dict com os itens coletados com o split

        return [int(formated[0]), f'{formated[-1]} {formated[-2]}']
    else:
        # retorna um dict com uma chave com o valor 0 para linhas e a quantidade de dados
        # return {'lines': 0, formated[1]: formated[0]}
        return [0, f'{formated[1]} {formated[0]}']
