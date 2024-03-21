import requests

import pandas as pd

from config import PROXIES, URL_WILD

PROXIES


def get_product():
    URL_WILD

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'ru,en;q=0.9',
        'Connection': 'keep-alive',
        'Origin': 'https://www.wildberries.ru',
        'Referer': 'https://www.wildberries.ru/catalog/elektronika/noutbuki-periferiya',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 YaBrowser/24.1.0.0 Safari/537.36',
        'sec-ch-ua': 'Not_A Brand";v="8", "Chromium";v="120", "YaBrowser";v="24.1", "Yowser";v="2.5',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': 'Windows',
    }

    response = requests.get(url=URL_WILD, headers=headers, proxies=PROXIES)
    return response.json()


def get_information(response):
    products = []

    products_dict = response.get('data', {}).get('products', None)

    if products_dict != None and len(products_dict) > 0:
        for product in products_dict:
            basic_price = float(product['sizes'][0].get(
                'price', {}).get('basic', None))
            price = float(product['sizes'][0].get(
                'price', {}).get('total', None))
            products.append({
                'Брэнд': product.get('brand', None),
                'Имя': product.get('name', None),
                'Цена без скидки': basic_price / 100,
                'Цена со скидкой': price / 100
            })

    return products


def main():
    response = get_product()
    products = get_information(response)
    df = pd.DataFrame(products)
    df.to_excel('products.xlsx', index=False)


if __name__ == '__main__':
    main()
