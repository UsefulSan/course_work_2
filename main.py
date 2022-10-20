import json
from typing import Any


def add_request() -> str:
    """
    String to create an sql table of suppliers and add a new column to the products table
    """
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
              f'homepage VARCHAR(100));\n' \
              f'ALTER TABLE products ADD id_suppliers INTEGER REFERENCES suppliers(id_suppliers);\n'
    return request


def load_suppliers() -> list[dict]:
    """
    Loads data from a json file
    :return: str data
    """
    with open('suppliers.json', encoding='utf-8') as file:
        row_suppliers = json.load(file)
        return row_suppliers


def split_suppliers(data: list[dict]) -> tuple[
    list[tuple[int, Any, str, str, str, str, str, str, str, Any, Any, Any]], list[list[Any]]]:
    """
    Formats the data
    :param data: process data
    :return: data in lists
    """
    id_suppliers = 0
    data_list = []
    product_list = []
    for d in data:
        id_suppliers += 1
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
        prod = [i.replace("'", "''") for i in d['products']]
        product_list.append(prod)
    return data_list, product_list


def write_request(request: str):
    """
    Append strings to the sql file
    """
    with open('suppliers.sql', 'w', encoding='utf-8') as file:
        file.write(request)


def write_suppliers(data: Any):
    """
    Write data to the sql file
    """
    with open('suppliers.sql', 'a', encoding='utf-8') as file:
        for d in data[0]:
            file.writelines(f'INSERT INTO suppliers VALUES {d};\n')


def write_products(data: Any):
    """
    Write data to the sql file
    """
    with open('suppliers.sql', 'a', encoding='utf-8') as file:
        counter = 0
        for d in data[1]:
            counter += 1
            file.writelines(
                f"""UPDATE products SET id_suppliers = {counter} WHERE product_name IN ('{"','".join(d)}');\n""")


def request_customers_page():
    """
    Write string to the sql file
    """
    with open('customers_page.sql', 'a', encoding='utf-8') as file:
        file.write("""SELECT COUNT (*) FROM (SELECT DISTINCT (city) FROM customers ORDER BY city ) AS foo;""")


def main():
    write_request(add_request())
    data_suppliers = load_suppliers()
    changed_data = split_suppliers(data_suppliers)
    write_suppliers(changed_data)
    write_products(changed_data)
    request_customers_page()


if __name__ == '__main__':
    main()
