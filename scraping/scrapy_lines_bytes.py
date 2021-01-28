from scraping.funtion import html_convert_python


def get_lines_bytes(url):
    obj_bs4 = html_convert_python(url)
