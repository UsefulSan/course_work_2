import json


def add_request():
    request = f'CREATE TABLE IF NOT EXISTS suppliers(' \
              f'id_suppliers SERIAL PRIMARY KEY, ' \
              f'company_name VARCHAR(70), ' \
              f'contact_name VARCHAR(70), ' \
              f'contact_title VARCHAR(70), ' \
              f'ad_county VARCHAR(70), ' \
              f'ad_state VARCHAR(70), ' \
              f'ad_index VARCHAR(70), ' \
              f'ad_city VARCHAR(70), ' \
              f'ad_street VARCHAR(70), ' \
              f'phone VARCHAR(70), ' \
              f'fax VARCHAR(70), ' \
              f'homepage VARCHAR(70));\n' \
              f'ALTER TABLE products ADD id_suppliers INTEGER REFERENCES suppliers(id_suppliers);\n'
    return request


def load_suppliers():
    with open('suppliers.json', encoding='utf-8') as file:
        row_suppliers = json.load(file)
        return row_suppliers


def split_suppliers(data):
    id_suppliers = 0
    data_list = []
    product_list = []
    for d in data:
        id_suppliers += 1
        products = d['products']
        products = (products)
        data_list.append((id_suppliers, d['company_name'].replace("'", "/"),
                          ''.join(d['contact'].split(',')[0]),
                          ''.join(d['contact'].split(',')[1]).lstrip(),
                          ''.join(d['address'].split(';')[0]),
                          ''.join(d['address'].split(';')[1]).lstrip(),
                          ''.join(d['address'].split(';')[2]).lstrip(),
                          ''.join(d['address'].split(';')[3]).lstrip(),
                          ''.join(d['address'].split(';')[4]).lstrip().replace("'", "/"),
                          d['phone'],
                          d['fax'],
                          d['homepage'].replace("'", "/")))
        # product_list.append(', '.join(d['products']).replace("'", "/"))
        product_list.append(d['products'])
        print(products)
        # print(d['fax'])
    # print(data_list)
    # print(product_list)
    return data_list, product_list

# .
# def do_id_for_products(data):
#     for d in data:
#         if d['products']:
#             pass


def write_request(request: str):
    """
    Добавляет строки в sql запрос
    """
    with open('suppliers.sql', 'w', encoding='utf-8') as file:
        file.write(request)


def write_suppliers(data):
    """
    Записывает данные в sql файл
    """
    with open('suppliers.sql', 'a', encoding='utf-8') as file:
        for d in data[0]:
            file.writelines(f'INSERT INTO suppliers VALUES {d};\n')


def write_products(data):
    with open('suppliers.sql', 'a', encoding='utf-8') as file:
        counter = 0
        for d in data[1]:
            counter += 1
            file.writelines(f"""UPDATE products SET id_suppliers = {counter} WHERE product_name IN ('{"','".join(d).replace("'", "/")}');\n""")


def main():
    write_request(add_request())
    data_suppliers = load_suppliers()
    changed_data = split_suppliers(data_suppliers)
    write_suppliers(changed_data)
    write_products(changed_data)


if __name__ == '__main__':
    main()
