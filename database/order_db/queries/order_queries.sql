-- ============================================
-- ORDER SERVICE QUERIES
-- ============================================

-- 1. View all orders
SELECT * FROM orders;


-- 2. View all order items
SELECT * FROM order_items;


-- 3. View all orders placed by a specific user
SELECT *
FROM orders
WHERE user_id = 1;


-- 4. View all delivered orders
SELECT *
FROM orders
WHERE order_status = 'Delivered';


-- 5. View orders with total amount greater than ₹50,000
SELECT *
FROM orders
WHERE total_amount > 50000;


-- 6. View complete order details with ordered products
SELECT
    o.order_id,
    o.user_id,
    o.total_amount,
    o.order_status,
    oi.product_id,
    oi.quantity,
    oi.price
FROM orders o
JOIN order_items oi
ON o.order_id = oi.order_id;