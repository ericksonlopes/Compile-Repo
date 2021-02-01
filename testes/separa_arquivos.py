from scraping.scrapy_data_full import get_data_repository_full

repo = 'docker/compose'
for item in get_data_repository_full(repo):

    if item['type_file'] == 'File':
        if f'/{repo}/tree/' in item['url'] or item['url'] == f'/{repo}':
            pass
        else:
            print(item['url'])
