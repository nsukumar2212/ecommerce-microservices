Low Level Design (LLD)

1. Purpose

The Low-Level Design (LLD) defines the internal architecture of each microservice, including project structure, API layers, request flow, database interaction, validation, and communication with other services.

2. Layered Architecture

Every microservice follows the same layered architecture.

Client

↓

Router Layer

↓

Service Layer

↓

CRUD / Repository Layer

↓

Model Layer

↓

Database 3. Common Folder Structure

Every service should follow the same structure.

service-name/

app/

routers/

services/

crud/

models/

schemas/

database/

config/

utils/

middleware/

main.py

database.py

requirements.txt

.env 4. Responsibilities of Each Layer
Router Layer

Responsibilities

Receive HTTP Request
Validate Route
Call Service Layer
Return Response

Example

POST /login

↓

login_router.py
Service Layer

Responsibilities

Business Logic
Validation
API Communication
Exception Handling

Example

Login User

↓

Validate Password

↓

Generate JWT

↓

Return Token
CRUD Layer

Responsibilities

SQL Queries
Insert
Update
Delete
Read

Example

SELECT

INSERT

UPDATE

DELETE
Model Layer

Responsibilities

Database Tables

Example

class User(Base):
Schema Layer

Responsibilities

Request Validation

Response Validation

Example

UserCreate

UserLogin

UserResponse
Utility Layer

Responsibilities

JWT

Password Hashing

Email

Common Functions

Middleware

Responsibilities

Authentication

Logging

Exception Handling

5. User Service Design
   user-service/

routers/
auth.py
profile.py
address.py

services/
auth_service.py
profile_service.py

crud/
user_crud.py
address_crud.py

models/
user.py
role.py
address.py

schemas/
user_schema.py
login_schema.py

utils/
jwt_handler.py
password.py
User Service Flow
Client

↓

POST /login

↓

Router

↓

Auth Service

↓

User CRUD

↓

Database

↓

JWT

↓

Response 6. Product Service Design
product-service/

routers/

services/

crud/

models/

schemas/

uploads/

Responsibilities

Products
Categories
Brands
Inventory
Reviews

Flow

GET /products

↓

Router

↓

Product Service

↓

CRUD

↓

Database

↓

Response 7. Cart Service Design

Responsibilities

Add Item
Remove Item
Update Quantity

Flow

Client

↓

Add Cart

↓

Cart Router

↓

Cart Service

↓

Product Service

(Check Product)

↓

Database 8. Order Service Design

Responsibilities

Place Order
Cancel Order
Track Order

Flow

Customer

↓

Order Router

↓

Order Service

↓

Product Service

↓

Payment Service

↓

Notification Service

↓

Database 9. Payment Service

Responsibilities

Verify Payment
Store Transaction
Refund

Flow

Payment Request

↓

Payment Service

↓

Mock Payment

↓

Database 10. Notification Service

Responsibilities

Email
SMS

Flow

Order Created

↓

Notification Service

↓

SMTP

↓

Customer 11. API Gateway

Responsibilities

Routing
JWT Validation
Logging
Authentication

Flow

React

↓

Gateway

↓

User Service

↓

Response 12. Request Lifecycle

Example

Customer Login

↓

React

↓

Gateway

↓

User Router

↓

Auth Service

↓

CRUD

↓

MySQL

↓

CRUD

↓

Service

↓

Router

↓

Gateway

↓

React 13. Exception Flow
Request

↓

Validation

↓

Business Logic

↓

Database

↓

Exception

↓

Global Exception Handler

↓

JSON Response 14. Standard API Response

Every API should return a consistent structure.

Success
{
"success": true,
"message": "Product created successfully",
"data": {}
}
Error
{
"success": false,
"message": "Product not found",
"errors": []
} 15. Naming Conventions
Files
user_router.py

user_service.py

user_crud.py

user_schema.py

user_model.py
Classes
UserService

UserCRUD

UserCreate

UserLogin

User
Functions
create_user()

login_user()

get_products()

update_product()

delete_order() 16. Logging Strategy

Every service logs:

Incoming Requests
Outgoing Responses
Exceptions
Authentication Events
Payment Transactions 17. Configuration

Use .env for:

DATABASE_URL=

JWT_SECRET=

JWT_ALGORITHM=

SMTP_HOST=

SMTP_PORT=

EMAIL=

PASSWORD= 18. Communication Between Services

All communication uses REST APIs.

Order Service

↓

GET Product

↓

Product Service

↓

POST Payment

↓

Payment Service

↓

POST Notification

↓

Notification Service 19. Deliverables

Your docs folder now contains:

docs/
├── Project_Overview.md
├── Software_Requirements_Specification.md
├── High_Level_Design.md
├── Database_Design.md
└── Low_Level_Design.md

# Low Level Design

## User Service

Architecture

Router
↓
Service
↓
CRUD
↓
SQLAlchemy Model
↓
MySQL

---

Authentication Flow

Client

↓

Register

↓

Password Hashing (bcrypt)

↓

MySQL

---

Login

↓

Verify Password

↓

JWT Generation

↓

Return Token

---

Protected APIs

JWT

↓

Verify Token

↓

Current User

↓

Business Logic

↓

Response

---

Implemented APIs

Authentication

- POST /auth/register
- POST /auth/login

Profile

- GET /users/me
- PUT /users/me
- PUT /users/change-password

Address

- POST /users/address
- GET /users/address
- PUT /users/address/{id}
- DELETE /users/address/{id}

Admin

- GET /admin/users
- GET /admin/users/{id}
- PUT /admin/users/{id}/role
- DELETE /admin/users/{id}

Security

- JWT Authentication
- Password Hashing
- RBAC
