import json

def read_data():
    with open ('data/categories.json', encoding='utf-8') as f:
        return json.load(f)


def get_product_by_id():
    products = read_data('data/products.json')