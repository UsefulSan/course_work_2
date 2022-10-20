-- Выбрать записи работников (включить колонки имени, фамилии, телефона, региона) в которых регион неизвестен

SELECT first_name, last_name, home_phone, region
FROM employees
WHERE region IS NULL;

-- Выбрать такие страны в которых "зарегистрированы" одновременно заказчики и поставщики,
-- но при этом в них не "зарегистрированы" работники

SELECT customers.country
FROM customers
INTERSECT
SELECT suppliers.ad_county
FROM suppliers
EXCEPT
SELECT employees.country
FROM employees;