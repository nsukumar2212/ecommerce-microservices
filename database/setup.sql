-- ==========================================================
-- E-Commerce Microservices Database Setup
-- Author : Sunny
-- ==========================================================

-- ==========================================================
-- USER SERVICE
-- ==========================================================

SOURCE user_db/schemas/user_db.sql;

USE user_db;

SOURCE user_db/tables/roles.sql;
SOURCE user_db/tables/users.sql;
SOURCE user_db/tables/addresses.sql;

SOURCE user_db/sample-data/roles_data.sql;
SOURCE user_db/sample-data/users_data.sql;
SOURCE user_db/sample-data/addresses_data.sql;


-- ==========================================================
-- PRODUCT SERVICE
-- ==========================================================

SOURCE product_db/schemas/product_db.sql;

USE product_db;

SOURCE product_db/tables/categories.sql;
SOURCE product_db/tables/products.sql;

SOURCE product_db/sample-data/categories_data.sql;
SOURCE product_db/sample-data/products_data.sql;


-- ==========================================================
-- CART SERVICE
-- ==========================================================

SOURCE cart_db/schemas/cart_db.sql;

USE cart_db;

SOURCE cart_db/tables/cart.sql;
SOURCE cart_db/tables/cart_items.sql;

SOURCE cart_db/sample-data/cart_data.sql;
SOURCE cart_db/sample-data/cart_items_data.sql;


-- ==========================================================
-- ORDER SERVICE
-- ==========================================================

SOURCE order_db/schemas/order_db.sql;

USE order_db;

SOURCE order_db/tables/orders.sql;
SOURCE order_db/tables/order_items.sql;

SOURCE order_db/sample-data/orders_data.sql;
SOURCE order_db/sample-data/order_items_data.sql;


-- ==========================================================
-- DATABASE SETUP COMPLETED
-- ==========================================================