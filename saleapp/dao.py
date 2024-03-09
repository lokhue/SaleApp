import json


def load_categories():
    with open('datas/categories.json', encoding='utf-8') as f:
        return json.load(f)


def load_products(q=None, cate_id=None):
    with open('datas/products.json', encoding='utf-8') as f:
        products = json.load(f)
        if q:
            products = [p for p in products if p['name'].lower().find(q.lower()) >= 0]
        if cate_id:
            products = [p for p in products if p['category_id'] == int(cate_id)]
        return products


def load_product_by_id(id):
    with open('datas/products.json', encoding='utf-8') as f:
        products = json.load(f)
        print(products)
        for p in products:
            if p['id'] == id:
                return p