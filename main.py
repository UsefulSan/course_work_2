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
        company_name = d['company_name']
        # contact_name = ''.join(d['contact'].split(',')[0])
        # contact_title = ''.join(d['contact'].split(',')[1])
        # ad_county = ''.join(d['address'].split(';')[0])
        # ad_state = ''.join(d['address'].split(';')[1])
        # ad_index = ''.join(d['address'].split(';')[2])
        # ad_city = ''.join(d['address'].split(';')[3])
        # ad_street = ''.join(d['address'].split(';')[4])
        # phone = d['phone']
        # fax = d['fax']
        # homepage = d['homepage']
        # products = d['products']
        # data_list.append(d['company_name']
        #              ''.join(d['contact'].split(',')[0]),
        #              ''.join(d['contact'].split(',')[1]),
        #              ''.join(d['address'].split(';')[0]),
        #              ''.join(d['address'].split(';')[1]),
        #              ''.join(d['address'].split(';')[2]),
        #              ''.join(d['address'].split(';')[3]),
        #              ''.join(d['address'].split(';')[4]),
        #              d['phone'],
        #              d['fax'],
        #              d['homepage'],
        #                 d['products'])
        print(company_name)

        # return company_name, contact_name, contact_title,\
        #        ad_county, ad_state, ad_index, ad_city, ad_street,\
        #        phone, fax, homepage, products



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
        # print(data)
        for row in data:
            print(data)
            file.write(f'INSERT INTO suppliers VALUES {row}')

def main():
    data_suppliers = load_suppliers()
    changed_data = split_suppliers(data_suppliers)
    # write_suppliers(changed_data)
if __name__ == '__main__':
    main()
