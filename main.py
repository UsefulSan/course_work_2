import json


def create_table():
    request = """
    CREATE TABLE IF NOT EXISTS suppliers(
    id_suppliers SERIAL PRIMARY KEY,
    company_name VARCHAR(70),
    contact_name VARCHAR(70),
    contact_title VARCHAR(70),
    ad_county VARCHAR(70),
    ad_state VARCHAR(70),
    ad_index VARCHAR(70),
    ad_city VARCHAR(70),
    ad_street VARCHAR(70),
    phone VARCHAR(70),
    fax VARCHAR(70),
    homepage VARCHAR(70));    
    """


def load_suppliers():
    with open('suppliers.json', encoding='utf-8') as file:
        row_suppliers = json.load(file)
        return row_suppliers


def split_suppliers(data):
    id_suppliers = 0
    data_list = []
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
    return data_list


def insert_into():
    """
    Добавляет строки в sql запрос
    :return:
    """
    pass


def write_suppliers(data):
    """
    Записывает данные в sql файл
    :return:
    """
    with open('suppliers.sql', 'w', encoding='utf-8') as file:
        for d in data:
            print(d)
            file.writelines(f'INSERT INTO suppliers VALUES {d}\n')


def main():
    data_suppliers = load_suppliers()
    changed_data = split_suppliers(data_suppliers)
    write_suppliers(changed_data)


if __name__ == '__main__':
    main()
