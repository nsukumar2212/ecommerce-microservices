USE cart_db;

-- ==========================================
-- Query 1 : View all carts
-- ==========================================

SELECT * FROM cart;

-- ==========================================
-- Query 2 : View all cart items
-- ==========================================

SELECT * FROM cart_items;

-- ==========================================
-- Query 3 : View all items in Cart 1
-- ==========================================

SELECT *
FROM cart_items
WHERE cart_id = 1;

-- ==========================================
-- Query 4 : Count products in Cart 1
-- ==========================================

SELECT COUNT(*) AS total_products
FROM cart_items
WHERE cart_id = 1;

-- ==========================================
-- Query 5 : Total quantity in Cart 1
-- ==========================================

SELECT SUM(quantity) AS total_quantity
FROM cart_items
WHERE cart_id = 1;

-- ==========================================
-- Query 6 : Products with quantity greater than 1
-- ==========================================

SELECT *
FROM cart_items
WHERE quantity > 1;