High Level Design (HLD)

1. Purpose

The High-Level Design document describes the overall architecture of the Scalable E-Commerce Platform. It defines the major components, their responsibilities, interactions, and technologies without going into implementation details.

2. System Architecture
   Internet
   │
   ▼
   React Frontend
   │
   HTTPS / REST API
   │
   ▼
   API Gateway
   │
   ┌──────────┬──────────┬──────────┬──────────┬──────────┬─────────────┐
   │ │ │ │ │ │
   ▼ ▼ ▼ ▼ ▼ ▼
   User Product Cart Order Payment Notification
   Service Service Service Service Service Service
   │ │ │ │ │ │
   ▼ ▼ ▼ ▼ ▼ ▼
   user_db product_db cart_db order_db payment_db notification_db
3. System Components
   Frontend

Technology

React.js
Bootstrap
Axios
React Router

Responsibilities

User Interface
Form Validation
API Calls
Authentication Token Storage
Dashboard
Checkout
API Gateway

Responsibilities

Receive all client requests
Validate JWT
Route requests
Centralized logging
Error handling
Rate limiting (future)
User Service

Responsibilities

User Registration
Login
JWT Authentication
User Profile
Address Management
Role Management

Database

user_db
Product Service

Responsibilities

Categories
Products
Brands
Inventory
Product Images
Reviews
Search

Database

product_db
Cart Service

Responsibilities

Add Item
Remove Item
Update Quantity
View Cart

Database

cart_db
Order Service

Responsibilities

Place Order
Order History
Track Order
Cancel Order

Database

order_db
Payment Service

Responsibilities

Payment Processing
Transaction Records
Refunds

Database

payment_db
Notification Service

Responsibilities

Email Notifications
SMS Notifications
Order Confirmation
Shipping Updates

Database

notification_db 4. Microservice Responsibilities
Service Responsibility Database
User Authentication & Profiles user_db
Product Products & Inventory product_db
Cart Shopping Cart cart_db
Order Orders order_db
Payment Payments payment_db
Notification Email/SMS notification_db
Gateway API Routing None 5. Communication Flow

All client requests pass through the API Gateway.

React

↓

API Gateway

↓

Target Microservice
Example: User Login
React

↓

Gateway

↓

User Service

↓

user_db
Example: Product Search
React

↓

Gateway

↓

Product Service

↓

product_db 6. Order Placement Flow
Customer

↓

React

↓

Gateway

↓

Order Service

↓

Product Service
(Check inventory)

↓

Payment Service
(Process payment)

↓

Notification Service
(Send email)

↓

Order Completed 7. Technology Stack
Layer Technology
Frontend React.js
Styling Bootstrap
Backend FastAPI
ORM SQLAlchemy
Validation Pydantic
Authentication JWT
Password Encryption bcrypt
Database MySQL
API Communication REST + HTTPX
API Documentation Swagger
Version Control Git & GitHub 8. Database Ownership

Each microservice owns its own database.

Database Owner
user_db User Service
product_db Product Service
cart_db Cart Service
order_db Order Service
payment_db Payment Service
notification_db Notification Service

A service must never directly access another service's database. If it needs data, it must call that service's API.

9. Security Design

Authentication

JWT Token

Authorization

Role-Based Access Control (Admin / Customer)

Password

bcrypt hashing

Communication

HTTPS (production) 10. Logging

Each service maintains its own logs.

Log types:

API Requests
API Responses
Errors
Authentication Events
Payment Transactions 11. Error Handling

Use consistent HTTP status codes.

Code Meaning
200 Success
201 Resource Created
400 Bad Request
401 Unauthorized
403 Forbidden
404 Not Found
409 Conflict
500 Internal Server Error 12. Deployment View

Initially (without Docker)

React
↓
localhost:5173

Gateway
↓
localhost:8000

User Service
↓
localhost:8001

Product Service
↓
localhost:8002

Cart Service
↓
localhost:8003

Order Service
↓
localhost:8004

Payment Service
↓
localhost:8005

Notification Service
↓
localhost:8006 13. Scalability Plan

Future enhancements include:

Docker
Docker Compose
Redis
RabbitMQ
Elasticsearch
Kubernetes
Prometheus
Grafana
CI/CD
