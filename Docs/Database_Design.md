Database Design

1. Purpose

This document defines the database architecture for the Scalable E-Commerce Platform. Each microservice owns its own database to ensure loose coupling, independent deployment, and scalability.

2. Database Architecture

Each microservice has a dedicated database.

Service Database
User Service user_db
Product Service product_db
Cart Service cart_db
Order Service order_db
Payment Service payment_db
Notification Service notification_db

Rule: A microservice must never directly access another service's database. Services communicate only through APIs.

3. Database List
   user_db

product_db

cart_db

order_db

payment_db

notification_db 4. Entity Relationship Overview
User
│
├── Address
│
├── Cart
│ │
│ └── Cart Items
│
├── Orders
│ │
│ ├── Order Items
│ │
│ └── Payment
│
└── Notifications

Product
│
├── Category
├── Brand
├── Inventory
├── Images
└── Reviews 5. user_db
Tables
users

roles

addresses
users
Column Type Constraint
id BIGINT PK
first_name VARCHAR(50) NOT NULL
last_name VARCHAR(50) NOT NULL
username VARCHAR(50) UNIQUE
email VARCHAR(100) UNIQUE
phone VARCHAR(15) UNIQUE
password VARCHAR(255) NOT NULL
role_id INT FK
status BOOLEAN DEFAULT TRUE
created_at DATETIME
updated_at DATETIME
roles
Column Type
id INT PK
role_name VARCHAR(30)
addresses
Column Type
id BIGINT PK
user_id BIGINT FK
address_line1 VARCHAR(200)
address_line2 VARCHAR(200)
city VARCHAR(100)
state VARCHAR(100)
country VARCHAR(100)
postal_code VARCHAR(15)
is_default BOOLEAN 6. product_db
Tables
categories

brands

products

product_images

inventory

reviews
products
Column Type
id BIGINT PK
category_id INT FK
brand_id INT FK
name VARCHAR(200)
description TEXT
price DECIMAL(10,2)
discount DECIMAL(5,2)
stock INT
sku VARCHAR(100)
status BOOLEAN
created_at DATETIME 7. cart_db

Tables

carts

cart_items
carts
Column Type
id BIGINT PK
user_id BIGINT
total_amount DECIMAL(10,2)
created_at DATETIME
cart_items
Column Type
id BIGINT PK
cart_id BIGINT FK
product_id BIGINT
quantity INT
price DECIMAL(10,2) 8. order_db

Tables

orders

order_items

order_tracking
orders
Column Type
id BIGINT PK
order_number VARCHAR(30) UNIQUE
user_id BIGINT
payment_id BIGINT
total DECIMAL(10,2)
order_status VARCHAR(30)
created_at DATETIME
order_items
Column Type
id BIGINT PK
order_id BIGINT FK
product_id BIGINT
quantity INT
price DECIMAL(10,2) 9. payment_db

Tables

payments

refunds
payments
Column Type
id BIGINT PK
order_id BIGINT
amount DECIMAL(10,2)
transaction_id VARCHAR(100)
payment_method VARCHAR(30)
payment_status VARCHAR(20)
payment_date DATETIME 10. notification_db

Tables

notifications

email_logs
notifications
Column Type
id BIGINT PK
user_id BIGINT
order_id BIGINT
type VARCHAR(30)
message TEXT
status VARCHAR(30)
created_at DATETIME 11. Primary Keys
Table Primary Key
users id
products id
carts id
orders id
payments id
notifications id 12. Foreign Keys
Table Foreign Key References
users role_id roles.id
addresses user_id users.id
products category_id categories.id
products brand_id brands.id
cart_items cart_id carts.id
order_items order_id orders.id

Note: In a microservices architecture, references to entities in other services (such as user_id in orders) are stored as IDs but are not enforced with database foreign keys. Validation is performed through service-to-service API calls.

13. Indexes

Create indexes for:

email
username
phone
product_name
sku
order_number
transaction_id 14. Constraints
Email must be unique.
Username must be unique.
SKU must be unique.
Quantity cannot be negative.
Price must be greater than zero.
Stock cannot be negative.
Payment must be successful before confirming an order. 15. Audit Columns

Every major table should include:

created_at

updated_at

created_by

updated_by

# Database Design

## User Service

### Tables

### Roles

| Column    | Type        | Constraints        |
| --------- | ----------- | ------------------ |
| role_id   | INT         | PK, AUTO_INCREMENT |
| role_name | VARCHAR(50) | UNIQUE             |

---

### Users

| Column     | Type         | Constraints               |
| ---------- | ------------ | ------------------------- |
| user_id    | INT          | PK, AUTO_INCREMENT        |
| full_name  | VARCHAR(100) | NOT NULL                  |
| email      | VARCHAR(100) | UNIQUE                    |
| password   | VARCHAR(255) | NOT NULL                  |
| phone      | VARCHAR(20)  | UNIQUE                    |
| role_id    | INT          | FK → Roles                |
| created_at | TIMESTAMP    | DEFAULT CURRENT_TIMESTAMP |

---

### Addresses

| Column       | Type         | Constraints               |
| ------------ | ------------ | ------------------------- |
| address_id   | INT          | PK                        |
| user_id      | INT          | FK → Users                |
| address_line | VARCHAR(255) | NOT NULL                  |
| city         | VARCHAR(100) | NOT NULL                  |
| state        | VARCHAR(100) | NOT NULL                  |
| pincode      | VARCHAR(20)  | NOT NULL                  |
| country      | VARCHAR(100) | NOT NULL                  |
| created_at   | TIMESTAMP    | DEFAULT CURRENT_TIMESTAMP |

---

## Relationships

Users (1)
│
│
├─────────────── (Many)
Addresses

Roles (1)
│
│
├─────────────── (Many)
Users
