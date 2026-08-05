-- ==========================================
-- E-Commerce Microservices Database Setup
-- ==========================================

-- ==========================
-- USER SERVICE
-- ==========================

SOURCE user_db/schemas/user_db.sql;

SOURCE user_db/tables/roles.sql;
SOURCE user_db/tables/users.sql;
SOURCE user_db/tables/addresses.sql;

SOURCE user_db/sample-data/roles_data.sql;
SOURCE user_db/sample-data/users_data.sql;
SOURCE user_db/sample-data/addresses_data.sql;

-- ==========================
-- PRODUCT SERVICE
-- ==========================

SOURCE product_db/schemas/product_db.sql;

SOURCE product_db/tables/categories.sql;
SOURCE product_db/tables/products.sql;

SOURCE product_db/sample-data/categories_data.sql;
SOURCE product_db/sample-data/products_data.sql;