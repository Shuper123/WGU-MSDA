-- List region names, sorted by total profits

SELECT sr.region_name, 
       SUM(a.total_profit) AS regional_profit
FROM accounting a
LEFT JOIN orders o 
       ON a.order_id = o.order_id
LEFT JOIN sale_region sr
       ON o.region_id = sr.region_id
GROUP BY sr.region_name
ORDER BY regional_profit DESC;




-- List product names, sorted by total quantity sold

SELECT p.product_name,
       SUM(o.product_quantity) AS total_quantities
FROM orders o
LEFT JOIN products p
       ON o.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_quantities DESC;




-- List product names, sorted by total profits

SELECT p.product_name,
       SUM(a.total_profit) AS product_profit
FROM accounting a
LEFT JOIN orders o
       ON a.order_id = o.order_id
LEFT JOIN products p
       ON o.product_id = p.product_id
GROUP BY p.product_name
ORDER BY product_profit DESC;




-- List region names, products sold therein, sorted by total profits

SELECT
  sr.region_name,
  p.product_name,
  SUM(a.total_profit) AS total_profit
FROM accounting a
JOIN orders o
  ON a.order_id = o.order_id
JOIN products p
  ON o.product_id = p.product_id
JOIN sale_region sr
  ON o.region_id = sr.region_id
GROUP BY sr.region_name, p.product_name
ORDER BY sr.region_name, total_profit DESC;




-- List individual products and their prices, sorted by price

SELECT product_name, profit 
FROM products
ORDER BY profit DESC




-- List Order IDs, date, profit and product sold from orders

SELECT o.order_id AS "Order ID", 
	o.order_date AS "Date",
	a.total_profit AS "Order Profit",
	p.product_name AS "Product Name"
FROM 
	accounting AS a
JOIN 
	orders AS o ON o.order_id = a.order_id
JOIN
	products AS p ON o.product_id = p.product_id;




-- List Product quantities by region

SELECT p.product_name AS Product, 
	SUM(o.product_quantity) AS Quantity, 
	r.region_name AS Region
FROM orders AS o
JOIN products AS p ON o.product_id = p.product_id
JOIN sale_region AS r ON o.region_id = r.region_id
GROUP BY Product, Region;