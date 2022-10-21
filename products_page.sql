-- Найти активные (см. поле discontinued) продукты из категории Beverages и Seafood, которых в продаже менее 20 единиц.
-- Вывести наименование продуктов, кол-во единиц в продаже, имя контакта поставщика и его телефонный номер

SELECT products.product_name, units_in_stock, contact_name, phone
FROM products
LEFT JOIN suppliers ON suppliers.id_suppliers = products.product_id
LEFT JOIN categories ON categories.category_id = products.category_id
WHERE (categories.category_name = 'Beverages' OR categories.category_name = 'Seafood')
  AND units_in_stock < 20 AND discontinued = 0;