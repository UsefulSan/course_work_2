-- Посчитать количество заказчиков

SELECT COUNT(customer_id)
FROM customers;

-- Выбрать все уникальные сочетания городов и стран, в которых "зарегистрированы" заказчики
SELECT city, customers.country
FROM customers
GROUP BY city, customers.country;

-- Найти заказчиков и обслуживающих их заказы сотрудников, таких, что и заказчики и сотрудники из города London,
-- а доставка идёт компанией Speedy Express. Вывести компанию заказчика и ФИО сотрудника.

SELECT customers.company_name, employees.last_name, employees.first_name
FROM orders
LEFT JOIN customers ON customers.customer_id = orders.customer_id
LEFT JOIN employees ON employees.employee_id = orders.employee_id
LEFT JOIN shippers ON shippers.shipper_id = orders.ship_via
WHERE customers.city = 'London' and employees.city = 'London' and shippers.company_name = 'Speedy Express';

-- Найти заказчиков, не сделавших ни одного заказа. Вывести имя заказчика и order_id

SELECT customers.company_name, orders.order_id
FROM customers
LEFT JOIN orders ON orders.customer_id = customers.customer_id
WHERE orders.order_id is NULL;
