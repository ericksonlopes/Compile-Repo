from scraping.funtion import html_convert_python
from scraping.scrapy_data_full import get_data_repository_full


def get_lines_bytes(url):
    obj_soup = html_convert_python(url)
    infos = obj_soup.find(class_='text-mono f6 flex-auto pr-3 flex-order-2 flex-md-order-1 mt-2 mt-md-0').text

    formated = infos.replace('symbolic link', '').replace('executable file', '').split()

    dict_return = {}

    if len(formated) == 6:
        # if formated[-1] ==
        convert_KB_bytes = formated[-2]
        # print(convert_KB_bytes)
        print({formated[1]: int(formated[0]), formated[-1]: formated[-2]})
    else:
        print({'lines': 0, formated[1]: formated[0]})
    # dict_return = {formated[0]: for}
    #
    # print(dict_return)

    # converter kb para bytes

    # return {'lines': 0, 'bytes': 0}


if __name__ == '__main__':

    repo = 'paulowiz/myportifolio'
    for item in get_data_repository_full(repo):

        if item['type_file'] == 'File':
            if f'/{repo}/tree/' in item['url'] or item['url'] == f'/{repo}':
                pass
            else:
                get_lines_bytes('https://github.com' + item['url']), item['url'], item['extension']
                # print(x, '\n')

    # 190 Bytes
    # 253 KB
    # for item in ['https://github.com/docker/compose/blob/master/project/RELEASE-PROCESS.md',
    #              'https://github.com/amoffat/sh/blob/develop/docker_test_suite/build.sh',
    #              'https://github.com/amoffat/sh/blob/develop/LICENSE.txt',
    #              'https://github.com/paulowiz/myportifolio/blob/main/static/assets/apple-icon-180x180.png']:
    #     get_lines_bytes(item)
