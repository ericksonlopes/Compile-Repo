from scraping.scrapy_lines_bytes import get_lines_bytes


def lines_bytes(item, repo, self):
    if f'/{repo}/tree/' in item['url'] or item['url'] == f'/{repo}':
        pass
    else:
        # converter tudo para Bytes
        item['lb'] = get_lines_bytes(self.url_git + item['url'])
        return item
