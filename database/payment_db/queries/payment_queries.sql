-- ============================================
-- PAYMENT SERVICE QUERIES
-- ============================================

-- 1. View all payments
SELECT * FROM payments;


-- 2. View successful payments
SELECT *
FROM payments
WHERE payment_status = 'Success';


-- 3. View pending payments
SELECT *
FROM payments
WHERE payment_status = 'Pending';


-- 4. View payments made using UPI
SELECT *
FROM payments
WHERE payment_method = 'UPI';


-- 5. View payments greater than ₹50,000
SELECT *
FROM payments
WHERE amount > 50000;


-- 6. View payment details for a specific order
SELECT *
FROM payments
WHERE order_id = 1;