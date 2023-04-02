import requests
from collections import Counter


def get_html(url: str) -> str:
    r = requests.get(url)
    return r.text


def count_symbols(text: str) -> list:
    symbols = Counter(text)
    return sorted(symbols.items())


if __name__ == "__main__":
    url = "https://www.python.org"
    html_text = get_html(url)
    result = count_symbols(html_text)
    print(f'{result}')
